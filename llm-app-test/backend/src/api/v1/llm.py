from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.models.user import User

router = APIRouter()


@router.get("/providers")
async def get_providers(
    current_user: User = Depends(get_current_user),
):
    """Get available LLM providers and models."""
    return {"message": "LLM providers endpoint - to be implemented"}


@router.post("/test-connection")
async def test_connection(
    current_user: User = Depends(get_current_user),
):
    """Test LLM provider connections."""
    return {"message": "Test connection endpoint - to be implemented"}


@router.post("/query")
async def query_llms(
    current_user: User = Depends(get_current_user),
):
    """Query multiple LLMs simultaneously."""
    return {"message": "Query LLMs endpoint - to be implemented"}