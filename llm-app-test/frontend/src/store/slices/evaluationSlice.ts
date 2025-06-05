import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface Evaluation {
  id: string;
  messageId: string;
  provider: string;
  userId: string;
  ratings: {
    usefulness: number;
    accuracy: number;
    creativity: number;
  };
  feedback?: string;
  timestamp: string;
}

export interface EvaluationStats {
  provider: string;
  averageRatings: {
    usefulness: number;
    accuracy: number;
    creativity: number;
  };
  totalEvaluations: number;
}

interface EvaluationState {
  evaluations: Evaluation[];
  stats: EvaluationStats[];
  isLoading: boolean;
  error: string | null;
}

const initialState: EvaluationState = {
  evaluations: [],
  stats: [],
  isLoading: false,
  error: null,
};

const evaluationSlice = createSlice({
  name: 'evaluation',
  initialState,
  reducers: {
    addEvaluation: (state, action: PayloadAction<Evaluation>) => {
      state.evaluations.push(action.payload);
    },
    setEvaluations: (state, action: PayloadAction<Evaluation[]>) => {
      state.evaluations = action.payload;
    },
    setStats: (state, action: PayloadAction<EvaluationStats[]>) => {
      state.stats = action.payload;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload;
    },
  },
});

export const { addEvaluation, setEvaluations, setStats, setLoading, setError } = evaluationSlice.actions;
export default evaluationSlice.reducer;