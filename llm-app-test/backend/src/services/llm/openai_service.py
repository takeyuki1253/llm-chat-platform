import openai
from typing import List, Dict, Any, Optional
import time
import asyncio
import logging
from .base import LLMProvider, LLMResponse

logger = logging.getLogger(__name__)


class OpenAIService(LLMProvider):
    AVAILABLE_MODELS = [
        "gpt-4",
        "gpt-4-turbo",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-16k"
    ]
    
    MODEL_COSTS = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-3.5-turbo": {"input": 0.0015, "output": 0.002},
        "gpt-3.5-turbo-16k": {"input": 0.003, "output": 0.004}
    }
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = openai.AsyncOpenAI(api_key=api_key)
    
    def get_provider_name(self) -> str:
        return "openai"
    
    def get_available_models(self) -> List[str]:
        return self.AVAILABLE_MODELS
    
    async def test_connection(self, api_key: str) -> bool:
        try:
            test_client = openai.AsyncOpenAI(api_key=api_key)
            response = await test_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            return response is not None
        except Exception as e:
            logger.error(f"OpenAI API connection test failed: {e}")
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
            
            response = await self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            response_time = time.time() - start_time
            
            content = response.choices[0].message.content if response.choices else ""
            tokens_used = response.usage.total_tokens if response.usage else None
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
            logger.error(f"OpenAI API error for model {model}: {e}")
            
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
        input_cost = usage.prompt_tokens * costs["input"] / 1000
        output_cost = usage.completion_tokens * costs["output"] / 1000
        
        return input_cost + output_cost
