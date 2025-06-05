from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from pydantic import BaseModel


class LLMResponse(BaseModel):
    content: str
    model: str
    provider: str
    tokens_used: Optional[int] = None
    response_time: Optional[float] = None
    cost: Optional[float] = None
    error: Optional[str] = None


class LLMProvider(ABC):
    @abstractmethod
    async def generate_response(self, prompt: str, model: str, **kwargs) -> LLMResponse:
        pass
    
    @abstractmethod
    def get_available_models(self) -> List[str]:
        pass
    
    @abstractmethod
    async def test_connection(self, api_key: str) -> bool:
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        pass
