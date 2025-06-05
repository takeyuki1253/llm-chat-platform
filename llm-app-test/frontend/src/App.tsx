import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Provider } from 'react-redux';
import { ThemeProvider, CssBaseline } from '@mui/material';
import { Toaster } from 'react-hot-toast';
import { store, useAppSelector, useAppDispatch } from '@store/index';
import { fetchCurrentUser } from '@store/slices/authSlice';
import { setTheme } from '@store/slices/uiSlice';
import { createTheme } from '@mui/material/styles';

// Pages
import HomePage from '@pages/HomePage';
import LoginPage from '@pages/LoginPage';
import ChatPage from '@pages/ChatPage';
import DashboardPage from '@pages/DashboardPage';
import SettingsPage from '@pages/SettingsPage';

// Components
import ProtectedRoute from '@components/auth/ProtectedRoute';
import Layout from '@components/common/Layout';

function AppContent() {
  const dispatch = useAppDispatch();
  const { theme } = useAppSelector((state) => state.ui);
  const { token } = useAppSelector((state) => state.auth);

  useEffect(() => {
    // Check for saved theme
    const savedTheme = localStorage.getItem('theme') as 'light' | 'dark';
    if (savedTheme) {
      dispatch(setTheme(savedTheme));
    }

    // Auto-login if token exists
    if (token) {
      dispatch(fetchCurrentUser());
    }
  }, [dispatch, token]);

  const muiTheme = createTheme({
    palette: {
      mode: theme,
      primary: {
        main: theme === 'light' ? '#0066e6' : '#4d9aff',
      },
      secondary: {
        main: theme === 'light' ? '#7300e6' : '#a64dff',
      },
    },
    typography: {
      fontFamily: 'Inter, system-ui, sans-serif',
    },
  });

  return (
    <ThemeProvider theme={muiTheme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Layout />
              </ProtectedRoute>
            }
          >
            <Route index element={<HomePage />} />
            <Route path="chat" element={<ChatPage />} />
            <Route path="chat/:sessionId" element={<ChatPage />} />
            <Route path="dashboard" element={<DashboardPage />} />
            <Route path="settings" element={<SettingsPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Router>
      <Toaster
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: theme === 'dark' ? '#1f2937' : '#fff',
            color: theme === 'dark' ? '#f3f4f6' : '#111827',
          },
        }}
      />
    </ThemeProvider>
  );
}

function App() {
  return (
    <Provider store={store}>
      <AppContent />
    </Provider>
  );
}

export default App;