import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface UsageStats {
  provider: string;
  model: string;
  date: string;
  requestCount: number;
  tokenCount: number;
  totalCost: number;
  averageResponseTime: number;
}

export interface DashboardMetrics {
  totalRequests: number;
  totalTokens: number;
  totalCost: number;
  averageResponseTime: number;
  errorRate: number;
}

interface DashboardState {
  usageStats: UsageStats[];
  metrics: DashboardMetrics;
  dateRange: {
    start: string;
    end: string;
  };
  isLoading: boolean;
  error: string | null;
}

const initialState: DashboardState = {
  usageStats: [],
  metrics: {
    totalRequests: 0,
    totalTokens: 0,
    totalCost: 0,
    averageResponseTime: 0,
    errorRate: 0,
  },
  dateRange: {
    start: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(),
    end: new Date().toISOString(),
  },
  isLoading: false,
  error: null,
};

const dashboardSlice = createSlice({
  name: 'dashboard',
  initialState,
  reducers: {
    setUsageStats: (state, action: PayloadAction<UsageStats[]>) => {
      state.usageStats = action.payload;
    },
    setMetrics: (state, action: PayloadAction<DashboardMetrics>) => {
      state.metrics = action.payload;
    },
    setDateRange: (state, action: PayloadAction<{ start: string; end: string }>) => {
      state.dateRange = action.payload;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload;
    },
  },
});

export const { setUsageStats, setMetrics, setDateRange, setLoading, setError } = dashboardSlice.actions;
export default dashboardSlice.reducer;