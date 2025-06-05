from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.models.user import User

router = APIRouter()


@router.get("/stats")
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
):
    """Get dashboard statistics."""
    return {"message": "Dashboard stats endpoint - to be implemented"}


@router.get("/usage")
async def get_usage_metrics(
    current_user: User = Depends(get_current_user),
):
    """Get usage metrics."""
    return {"message": "Usage metrics endpoint - to be implemented"}


@router.get("/costs")
async def get_cost_analysis(
    current_user: User = Depends(get_current_user),
):
    """Get cost analysis."""
    return {"message": "Cost analysis endpoint - to be implemented"}