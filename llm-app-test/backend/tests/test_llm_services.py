import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from src.services.llm.google_service import GoogleService
from src.services.llm.coordinator import LLMCoordinator
from src.services.llm.base import LLMResponse


class TestGoogleService:
    def test_get_available_models(self):
        service = GoogleService("test-api-key")
        models = service.get_available_models()
        
        expected_models = [
            "gemini-pro",
            "gemini-pro-vision", 
            "gemini-1.5-pro",
            "gemini-1.5-flash"
        ]
        
        assert models == expected_models
    
    def test_get_provider_name(self):
        service = GoogleService("test-api-key")
        assert service.get_provider_name() == "google"
    
    @pytest.mark.asyncio
    async def test_generate_response_invalid_model(self):
        service = GoogleService("test-api-key")
        response = await service.generate_response("test prompt", "invalid-model")
        
        assert response.content == ""
        assert response.model == "invalid-model"
        assert response.provider == "google"
        assert response.error == "Model invalid-model not available"


class TestLLMCoordinator:
    def test_init_with_google_key(self):
        api_keys = {"google": "test-google-key"}
        coordinator = LLMCoordinator(api_keys)
        
        assert "google" in coordinator.providers
        assert isinstance(coordinator.providers["google"], GoogleService)
    
    def test_init_without_keys(self):
        coordinator = LLMCoordinator({})
        assert len(coordinator.providers) == 0
    
    def test_get_available_providers(self):
        api_keys = {"google": "test-google-key"}
        coordinator = LLMCoordinator(api_keys)
        
        providers = coordinator.get_available_providers()
        assert "google" in providers
        assert len(providers["google"]) == 4
    
    @pytest.mark.asyncio
    async def test_query_multiple_models_no_models(self):
        coordinator = LLMCoordinator({})
        responses = await coordinator.query_multiple_models("test", [])
        assert responses == []
    
    @pytest.mark.asyncio
    async def test_query_multiple_models_invalid_provider(self):
        coordinator = LLMCoordinator({})
        selected_models = [{"provider": "invalid", "model": "test"}]
        
        responses = await coordinator.query_multiple_models("test", selected_models)
        assert len(responses) == 1
        assert responses[0].error == "Provider invalid not configured"
