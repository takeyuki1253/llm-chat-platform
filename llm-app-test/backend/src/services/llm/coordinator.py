import asyncio
from typing import List, Dict, Any, Optional
import logging
from .google_service import GoogleService
from .openai_service import OpenAIService
from .anthropic_service import AnthropicService
from .base import LLMResponse

logger = logging.getLogger(__name__)


class LLMCoordinator:
    def __init__(self, user_api_keys: Dict[str, str]):
        self.providers = {}
        
        if user_api_keys.get("google"):
            self.providers["google"] = GoogleService(user_api_keys["google"])
        if user_api_keys.get("openai"):
            self.providers["openai"] = OpenAIService(user_api_keys["openai"])
        if user_api_keys.get("anthropic"):
            self.providers["anthropic"] = AnthropicService(user_api_keys["anthropic"])
    
    def get_available_providers(self) -> Dict[str, List[str]]:
        result = {}
        for provider_name, provider in self.providers.items():
            result[provider_name] = provider.get_available_models()
        return result
    
    async def test_connections(self, api_keys: Dict[str, str]) -> Dict[str, bool]:
        results = {}
        
        if "google" in api_keys and "google" in self.providers:
            results["google"] = await self.providers["google"].test_connection(api_keys["google"])
        if "openai" in api_keys and "openai" in self.providers:
            results["openai"] = await self.providers["openai"].test_connection(api_keys["openai"])
        if "anthropic" in api_keys and "anthropic" in self.providers:
            results["anthropic"] = await self.providers["anthropic"].test_connection(api_keys["anthropic"])
        
        return results
    
    async def query_multiple_models(
        self, 
        prompt: str, 
        selected_models: List[Dict[str, str]], 
        **kwargs
    ) -> List[LLMResponse]:
        tasks = []
        
        for model_config in selected_models:
            provider_name = model_config.get("provider")
            model_name = model_config.get("model")
            
            if provider_name in self.providers:
                provider = self.providers[provider_name]
                task = provider.generate_response(prompt, model_name, **kwargs)
                tasks.append(task)
            else:
                error_response = LLMResponse(
                    content="",
                    model=model_name,
                    provider=provider_name,
                    error=f"Provider {provider_name} not configured"
                )
                tasks.append(asyncio.create_task(self._return_error(error_response)))
        
        if not tasks:
            return []
        
        try:
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            result = []
            for response in responses:
                if isinstance(response, Exception):
                    logger.error(f"Task failed with exception: {response}")
                    result.append(LLMResponse(
                        content="",
                        model="unknown",
                        provider="unknown",
                        error=str(response)
                    ))
                else:
                    result.append(response)
            
            return result
            
        except Exception as e:
            logger.error(f"Error in parallel execution: {e}")
            return [LLMResponse(
                content="",
                model="unknown",
                provider="unknown",
                error=f"Coordinator error: {str(e)}"
            )]
    
    async def _return_error(self, error_response: LLMResponse) -> LLMResponse:
        return error_response
