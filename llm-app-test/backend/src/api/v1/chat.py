from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.models.user import User

router = APIRouter()


@router.get("/sessions")
async def get_chat_sessions(
    current_user: User = Depends(get_current_user),
):
    """Get user's chat sessions."""
    return {"message": "Chat sessions endpoint - to be implemented"}


@router.post("/sessions")
async def create_chat_session(
    current_user: User = Depends(get_current_user),
):
    """Create a new chat session."""
    return {"message": "Create chat session endpoint - to be implemented"}


@router.get("/sessions/{session_id}/messages")
async def get_messages(
    session_id: str,
    current_user: User = Depends(get_current_user),
):
    """Get messages for a chat session."""
    return {"message": "Get messages endpoint - to be implemented"}


@router.post("/sessions/{session_id}/messages")
async def send_message(
    session_id: str,
    current_user: User = Depends(get_current_user),
):
    """Send a message to multiple LLMs."""
    return {"message": "Send message endpoint - to be implemented"}