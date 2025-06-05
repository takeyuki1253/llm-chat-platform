from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.models.user import User

router = APIRouter()


@router.post("/rate")
async def rate_response(
    current_user: User = Depends(get_current_user),
):
    """Rate an LLM response."""
    return {"message": "Rate response endpoint - to be implemented"}


@router.get("/stats")
async def get_evaluation_stats(
    current_user: User = Depends(get_current_user),
):
    """Get evaluation statistics."""
    return {"message": "Evaluation stats endpoint - to be implemented"}


@router.get("/history")
async def get_evaluation_history(
    current_user: User = Depends(get_current_user),
):
    """Get evaluation history."""
    return {"message": "Evaluation history endpoint - to be implemented"}