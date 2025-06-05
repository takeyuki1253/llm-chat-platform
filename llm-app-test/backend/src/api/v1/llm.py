from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import time
from typing import Dict, Any

from src.core.deps import get_current_user, get_db
from src.models.user import User
from src.schemas.llm import (
    LLMQueryRequest, 
    LLMQueryResponse, 
    ProvidersResponse, 
    ProviderInfo,
    ConnectionTestRequest,
    ConnectionTestResponse,
    LLMResponseData
)
from src.services.llm import LLMCoordinator
from src.config.settings import settings

router = APIRouter()


def _get_user_api_keys(user: User) -> Dict[str, str]:
    """Extract API keys from user data."""
    api_keys = {}
    if user.api_keys:
        if user.api_keys.get("google"):
            api_keys["google"] = user.api_keys["google"]
        if user.api_keys.get("openai"):
            api_keys["openai"] = user.api_keys["openai"]
        if user.api_keys.get("anthropic"):
            api_keys["anthropic"] = user.api_keys["anthropic"]
    return api_keys


@router.get("/providers", response_model=ProvidersResponse)
async def get_providers(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get available LLM providers and models."""
    try:
        user_api_keys = _get_user_api_keys(current_user)
        coordinator = LLMCoordinator(user_api_keys)
        
        available_providers = coordinator.get_available_providers()
        connection_status = await coordinator.test_connections(user_api_keys)
        
        providers = []
        for provider_name, models in available_providers.items():
            providers.append(ProviderInfo(
                name=provider_name,
                models=models,
                connected=connection_status.get(provider_name, False)
            ))
        
        return ProvidersResponse(providers=providers)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get providers: {str(e)}"
        )


@router.post("/test-connection", response_model=ConnectionTestResponse)
async def test_connection(
    request: ConnectionTestRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Test LLM provider connections."""
    try:
        test_api_keys = {request.provider: request.api_key}
        coordinator = LLMCoordinator(test_api_keys)
        
        connection_results = await coordinator.test_connections(test_api_keys)
        connected = connection_results.get(request.provider, False)
        
        return ConnectionTestResponse(
            provider=request.provider,
            connected=connected,
            error=None if connected else "Connection failed"
        )
        
    except Exception as e:
        return ConnectionTestResponse(
            provider=request.provider,
            connected=False,
            error=str(e)
        )


@router.post("/query", response_model=LLMQueryResponse)
async def query_llms(
    request: LLMQueryRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Query multiple LLMs simultaneously."""
    try:
        if not request.models:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one model must be specified"
            )
        
        user_api_keys = _get_user_api_keys(current_user)
        coordinator = LLMCoordinator(user_api_keys)
        
        start_time = time.time()
        
        selected_models = [
            {"provider": model.provider, "model": model.model}
            for model in request.models
        ]
        
        responses = await coordinator.query_multiple_models(
            prompt=request.prompt,
            selected_models=selected_models,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        total_time = time.time() - start_time
        total_cost = sum(r.cost for r in responses if r.cost is not None)
        
        response_data = [
            LLMResponseData(
                content=r.content,
                model=r.model,
                provider=r.provider,
                tokens_used=r.tokens_used,
                response_time=r.response_time,
                cost=r.cost,
                error=r.error
            )
            for r in responses
        ]
        
        return LLMQueryResponse(
            responses=response_data,
            total_time=total_time,
            total_cost=total_cost if total_cost > 0 else None
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to query LLMs: {str(e)}"
        )
