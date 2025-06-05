# Add Multiple Vertex AI Model Support to LLM Chat Platform

## Overview
This PR implements comprehensive support for multiple Vertex AI models in the LLM Chat Platform, extending the existing architecture to support parallel querying of different Google Generative AI models.

## Changes Made

### 🚀 New Features
- **Multiple Vertex AI Model Support**: Added support for 4 Vertex AI models:
  - `gemini-pro`: General purpose text generation
  - `gemini-pro-vision`: Multimodal capabilities  
  - `gemini-1.5-pro`: Latest high-performance model
  - `gemini-1.5-flash`: Fast, efficient model

- **Complete LLM Service Architecture**: Implemented the full LLM integration layer as specified in the Claude Code Guide:
  - Base `LLMProvider` abstract class for extensibility
  - `GoogleService` implementation with multiple model support
  - `OpenAIService` and `AnthropicService` for future multi-provider support
  - `LLMCoordinator` for parallel processing across providers and models

### 🏗️ Architecture Implementation
- **Service Layer**: Created `/backend/src/services/llm/` directory with modular provider implementations
- **Async Processing**: Full async/await support for parallel model querying
- **Error Handling**: Comprehensive error handling with detailed error responses
- **Cost Tracking**: Token usage and cost calculation for each model
- **Response Metrics**: Response time tracking and performance monitoring

### 📝 API Enhancements
- **Updated LLM Endpoints**: Replaced placeholder implementations with full functionality:
  - `GET /api/v1/llm/providers`: List available providers and models with connection status
  - `POST /api/v1/llm/test-connection`: Test API key connections for providers
  - `POST /api/v1/llm/query`: Query multiple models simultaneously with parallel processing

### 🔧 Configuration Updates
- **Settings**: Added `GOOGLE_VERTEX_MODELS` configuration for supported models
- **User Schema**: Extended `ApiKeysUpdate` to support model-specific configurations
- **Request/Response Schemas**: New comprehensive schemas for LLM operations

### 🧪 Testing
- **Unit Tests**: Added comprehensive test suite for service layer
- **Integration Tests**: Tests for coordinator and multi-model functionality
- **Error Scenarios**: Tests for invalid models, missing API keys, and connection failures

## Technical Details

### Supported Vertex AI Models
```python
AVAILABLE_MODELS = [
    "gemini-pro",           # General purpose, balanced performance
    "gemini-pro-vision",    # Multimodal with image understanding
    "gemini-1.5-pro",       # Latest high-performance model
    "gemini-1.5-flash"      # Fast, efficient for quick responses
]
```

### Usage Example
```python
# Query multiple Vertex AI models simultaneously
request = {
    "prompt": "Explain quantum computing",
    "models": [
        {"provider": "google", "model": "gemini-pro"},
        {"provider": "google", "model": "gemini-1.5-pro"},
        {"provider": "google", "model": "gemini-1.5-flash"}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}
```

### Performance Features
- **Parallel Execution**: All selected models are queried simultaneously using `asyncio.gather()`
- **Response Time Tracking**: Individual and total response times measured
- **Cost Calculation**: Automatic cost estimation based on token usage and model pricing
- **Error Isolation**: Individual model failures don't affect other model responses

## Files Changed
- `backend/src/services/llm/` - New service layer implementation
- `backend/src/schemas/llm.py` - New LLM request/response schemas
- `backend/src/api/v1/llm.py` - Complete endpoint implementation
- `backend/src/config/settings.py` - Added Vertex AI model configuration
- `backend/src/schemas/user.py` - Extended API key management
- `backend/tests/test_llm_services.py` - Comprehensive test suite

## Testing Performed
✅ Unit tests for all service classes  
✅ Integration tests for coordinator functionality  
✅ API endpoint testing with multiple models  
✅ Error handling validation  
✅ Performance testing with parallel requests  

## Breaking Changes
None - This is a pure feature addition that maintains backward compatibility.

## Dependencies
- Existing `google-generativeai==0.8.3` dependency utilized
- No new external dependencies added

---

**Link to Devin run**: https://app.devin.ai/sessions/3277a7a237574f08a1361b3fa83e430b

**Requested by**: takeumi (takeyuki.u.1253@gmail.com)
