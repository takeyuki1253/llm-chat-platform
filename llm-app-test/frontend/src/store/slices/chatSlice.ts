import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface Message {
  id: string;
  sessionId: string;
  content: string;
  type: 'user' | 'assistant';
  timestamp: string;
  responses?: LLMResponse[];
}

export interface LLMResponse {
  provider: 'openai' | 'google' | 'anthropic';
  model: string;
  content: string;
  responseTime: number;
  tokenCount: number;
  cost: number;
  error?: string;
}

export interface ChatSession {
  id: string;
  title: string;
  tags: string[];
  createdAt: string;
  updatedAt: string;
}

interface ChatState {
  sessions: ChatSession[];
  currentSessionId: string | null;
  messages: Message[];
  isLoading: boolean;
  error: string | null;
}

const initialState: ChatState = {
  sessions: [],
  currentSessionId: null,
  messages: [],
  isLoading: false,
  error: null,
};

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    setCurrentSession: (state, action: PayloadAction<string>) => {
      state.currentSessionId = action.payload;
    },
    addMessage: (state, action: PayloadAction<Message>) => {
      state.messages.push(action.payload);
    },
    updateMessageResponse: (state, action: PayloadAction<{ messageId: string; response: LLMResponse }>) => {
      const message = state.messages.find(m => m.id === action.payload.messageId);
      if (message) {
        if (!message.responses) {
          message.responses = [];
        }
        const existingIndex = message.responses.findIndex(r => r.provider === action.payload.response.provider);
        if (existingIndex !== -1) {
          message.responses[existingIndex] = action.payload.response;
        } else {
          message.responses.push(action.payload.response);
        }
      }
    },
    setSessions: (state, action: PayloadAction<ChatSession[]>) => {
      state.sessions = action.payload;
    },
    setMessages: (state, action: PayloadAction<Message[]>) => {
      state.messages = action.payload;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload;
    },
  },
});

export const {
  setCurrentSession,
  addMessage,
  updateMessageResponse,
  setSessions,
  setMessages,
  setLoading,
  setError,
} = chatSlice.actions;

export default chatSlice.reducer;