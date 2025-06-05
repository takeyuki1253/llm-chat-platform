import google.generativeai as genai
from typing import List, Dict, Any, Optional
import time
import asyncio
import logging
from .base import LLMProvider, LLMResponse

logger = logging.getLogger(__name__)


class GoogleService(LLMProvider):
    AVAILABLE_MODELS = [
        "gemini-pro",
        "gemini-pro-vision", 
        "gemini-1.5-pro",
        "gemini-1.5-flash"
    ]
    
    MODEL_COSTS = {
        "gemini-pro": {"input": 0.0005, "output": 0.0015},
        "gemini-pro-vision": {"input": 0.0005, "output": 0.0015},
        "gemini-1.5-pro": {"input": 0.0035, "output": 0.0105},
        "gemini-1.5-flash": {"input": 0.00035, "output": 0.00105}
    }
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        genai.configure(api_key=api_key)
    
    def get_provider_name(self) -> str:
        return "google"
    
    def get_available_models(self) -> List[str]:
        return self.AVAILABLE_MODELS
    
    async def test_connection(self, api_key: str) -> bool:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = await asyncio.to_thread(
                model.generate_content, 
                "Hello"
            )
            return response is not None
        except Exception as e:
            logger.error(f"Google API connection test failed: {e}")
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
            
            generation_config = genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
            
            genai_model = genai.GenerativeModel(
                model_name=model,
                generation_config=generation_config
            )
            
            response = await asyncio.to_thread(
                genai_model.generate_content,
                prompt
            )
            
            response_time = time.time() - start_time
            
            content = response.text if response.text else ""
            tokens_used = self._estimate_tokens(prompt, content)
            cost = self._calculate_cost(model, tokens_used)
            
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
            logger.error(f"Google API error for model {model}: {e}")
            
            return LLMResponse(
                content="",
                model=model,
                provider=self.get_provider_name(),
                response_time=response_time,
                error=str(e)
            )
    
    def _estimate_tokens(self, prompt: str, response: str) -> int:
        return len(prompt.split()) + len(response.split())
    
    def _calculate_cost(self, model: str, tokens: int) -> Optional[float]:
        if model not in self.MODEL_COSTS:
            return None
        
        input_tokens = tokens // 2
        output_tokens = tokens - input_tokens
        
        costs = self.MODEL_COSTS[model]
        return (input_tokens * costs["input"] + output_tokens * costs["output"]) / 1000
