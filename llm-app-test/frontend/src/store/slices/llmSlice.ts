import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface LLMProvider {
  id: 'openai' | 'google' | 'anthropic';
  name: string;
  models: LLMModel[];
  isEnabled: boolean;
  apiKeyConfigured: boolean;
}

export interface LLMModel {
  id: string;
  name: string;
  maxTokens: number;
  costPer1kTokens: number;
}

interface LLMSettings {
  temperature: number;
  maxTokens: number;
  topP: number;
  selectedModels: string[];
}

interface LLMState {
  providers: LLMProvider[];
  settings: LLMSettings;
  isQuerying: boolean;
}

const initialState: LLMState = {
  providers: [
    {
      id: 'openai',
      name: 'OpenAI',
      models: [
        { id: 'gpt-4', name: 'GPT-4', maxTokens: 8192, costPer1kTokens: 0.03 },
        { id: 'gpt-3.5-turbo', name: 'GPT-3.5 Turbo', maxTokens: 4096, costPer1kTokens: 0.001 },
      ],
      isEnabled: true,
      apiKeyConfigured: false,
    },
    {
      id: 'google',
      name: 'Google',
      models: [
        { id: 'gemini-pro', name: 'Gemini Pro', maxTokens: 32768, costPer1kTokens: 0.001 },
      ],
      isEnabled: true,
      apiKeyConfigured: false,
    },
    {
      id: 'anthropic',
      name: 'Anthropic',
      models: [
        { id: 'claude-3-opus', name: 'Claude 3 Opus', maxTokens: 200000, costPer1kTokens: 0.015 },
        { id: 'claude-3-sonnet', name: 'Claude 3 Sonnet', maxTokens: 200000, costPer1kTokens: 0.003 },
        { id: 'claude-3-haiku', name: 'Claude 3 Haiku', maxTokens: 200000, costPer1kTokens: 0.0025 },
      ],
      isEnabled: true,
      apiKeyConfigured: false,
    },
  ],
  settings: {
    temperature: 0.7,
    maxTokens: 2048,
    topP: 1.0,
    selectedModels: ['gpt-4', 'gemini-pro', 'claude-3-sonnet'],
  },
  isQuerying: false,
};

const llmSlice = createSlice({
  name: 'llm',
  initialState,
  reducers: {
    updateProviderStatus: (state, action: PayloadAction<{ providerId: string; isEnabled: boolean }>) => {
      const provider = state.providers.find(p => p.id === action.payload.providerId);
      if (provider) {
        provider.isEnabled = action.payload.isEnabled;
      }
    },
    updateApiKeyStatus: (state, action: PayloadAction<{ providerId: string; configured: boolean }>) => {
      const provider = state.providers.find(p => p.id === action.payload.providerId);
      if (provider) {
        provider.apiKeyConfigured = action.payload.configured;
      }
    },
    updateSettings: (state, action: PayloadAction<Partial<LLMSettings>>) => {
      state.settings = { ...state.settings, ...action.payload };
    },
    setQuerying: (state, action: PayloadAction<boolean>) => {
      state.isQuerying = action.payload;
    },
  },
});

export const { updateProviderStatus, updateApiKeyStatus, updateSettings, setQuerying } = llmSlice.actions;
export default llmSlice.reducer;