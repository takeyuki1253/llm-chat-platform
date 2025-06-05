import { apiClient } from './client';

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  password: string;
  name: string;
}

export interface AuthResponse {
  token: string;
  user: {
    id: string;
    email: string;
    name: string;
    apiKeys?: {
      openai?: string;
      google?: string;
      anthropic?: string;
    };
    settings?: Record<string, any>;
  };
}

export interface User {
  id: string;
  email: string;
  name: string;
  apiKeys?: {
    openai?: string;
    google?: string;
    anthropic?: string;
  };
  settings?: Record<string, any>;
}

class AuthService {
  async login(email: string, password: string): Promise<AuthResponse> {
    return apiClient.post<AuthResponse>('/api/v1/auth/login', { email, password });
  }

  async register(email: string, password: string, name: string): Promise<AuthResponse> {
    return apiClient.post<AuthResponse>('/api/v1/auth/register', { email, password, name });
  }

  async logout(): Promise<void> {
    return apiClient.post('/api/v1/auth/logout');
  }

  async getCurrentUser(): Promise<User> {
    return apiClient.get<User>('/api/v1/auth/me');
  }

  async updateApiKeys(apiKeys: Partial<User['apiKeys']>): Promise<User> {
    return apiClient.patch<User>('/api/v1/auth/api-keys', { apiKeys });
  }

  async updateProfile(data: Partial<User>): Promise<User> {
    return apiClient.patch<User>('/api/v1/auth/profile', data);
  }

  async changePassword(currentPassword: string, newPassword: string): Promise<void> {
    return apiClient.post('/api/v1/auth/change-password', {
      currentPassword,
      newPassword,
    });
  }
}

export const authService = new AuthService();