from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class ModelSelection(BaseModel):
    provider: str
    model: str


class LLMQueryRequest(BaseModel):
    prompt: str
    models: List[ModelSelection]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000


class LLMResponseData(BaseModel):
    content: str
    model: str
    provider: str
    tokens_used: Optional[int] = None
    response_time: Optional[float] = None
    cost: Optional[float] = None
    error: Optional[str] = None


class LLMQueryResponse(BaseModel):
    responses: List[LLMResponseData]
    total_time: float
    total_cost: Optional[float] = None


class ProviderInfo(BaseModel):
    name: str
    models: List[str]
    connected: bool


class ProvidersResponse(BaseModel):
    providers: List[ProviderInfo]


class ConnectionTestRequest(BaseModel):
    provider: str
    api_key: str


class ConnectionTestResponse(BaseModel):
    provider: str
    connected: bool
    error: Optional[str] = None
