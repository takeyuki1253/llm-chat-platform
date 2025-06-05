from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.models.user import User

router = APIRouter()


@router.get("/")
async def get_use_cases(
    current_user: User = Depends(get_current_user),
):
    """Get user's use cases."""
    return {"message": "Use cases endpoint - to be implemented"}


@router.post("/")
async def create_use_case(
    current_user: User = Depends(get_current_user),
):
    """Create a new use case."""
    return {"message": "Create use case endpoint - to be implemented"}


@router.put("/{use_case_id}")
async def update_use_case(
    use_case_id: str,
    current_user: User = Depends(get_current_user),
):
    """Update a use case."""
    return {"message": "Update use case endpoint - to be implemented"}


@router.post("/{use_case_id}/execute")
async def execute_use_case(
    use_case_id: str,
    current_user: User = Depends(get_current_user),
):
    """Execute a use case."""
    return {"message": "Execute use case endpoint - to be implemented"}