import anthropic
from typing import List, Dict, Any, Optional
import time
import asyncio
import logging
from .base import LLMProvider, LLMResponse

logger = logging.getLogger(__name__)


class AnthropicService(LLMProvider):
    AVAILABLE_MODELS = [
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-haiku-20240307"
    ]
    
    MODEL_COSTS = {
        "claude-3-opus-20240229": {"input": 0.015, "output": 0.075},
        "claude-3-sonnet-20240229": {"input": 0.003, "output": 0.015},
        "claude-3-haiku-20240307": {"input": 0.00025, "output": 0.00125}
    }
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
    
    def get_provider_name(self) -> str:
        return "anthropic"
    
    def get_available_models(self) -> List[str]:
        return self.AVAILABLE_MODELS
    
    async def test_connection(self, api_key: str) -> bool:
        try:
            test_client = anthropic.AsyncAnthropic(api_key=api_key)
            response = await test_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=5,
                messages=[{"role": "user", "content": "Hello"}]
            )
            return response is not None
        except Exception as e:
            logger.error(f"Anthropic API connection test failed: {e}")
            return False
    
    async def generate_response(self, prompt: str, model: str, **kwargs) -> LLMResponse:
        start_time = time.time()
        
        try:
            if model not in self.AVAILABLE_MODELS:
                return LLMResponse(
                    content="",
                    model=model,
                    provider=self.get_provider_name(),
                    error=f"Model {model} not available"
                )
            
            temperature = kwargs.get("temperature", 0.7)
            max_tokens = kwargs.get("max_tokens", 1000)
            
            response = await self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_time = time.time() - start_time
            
            content = response.content[0].text if response.content else ""
            tokens_used = response.usage.input_tokens + response.usage.output_tokens if response.usage else None
            cost = self._calculate_cost(model, response.usage) if response.usage else None
            
            return LLMResponse(
                content=content,
                model=model,
                provider=self.get_provider_name(),
                tokens_used=tokens_used,
                response_time=response_time,
                cost=cost
            )
            
        except Exception as e:
            response_time = time.time() - start_time
            logger.error(f"Anthropic API error for model {model}: {e}")
            
            return LLMResponse(
                content="",
                model=model,
                provider=self.get_provider_name(),
                response_time=response_time,
                error=str(e)
            )
    
    def _calculate_cost(self, model: str, usage) -> Optional[float]:
        if model not in self.MODEL_COSTS or not usage:
            return None
        
        costs = self.MODEL_COSTS[model]
        input_cost = usage.input_tokens * costs["input"] / 1000
        output_cost = usage.output_tokens * costs["output"] / 1000
        
        return input_cost + output_cost
