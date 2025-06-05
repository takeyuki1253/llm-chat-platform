import { useState } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import {
  Box,
  Paper,
  TextField,
  Button,
  Typography,
  Link,
  CircularProgress,
  Alert,
} from '@mui/material';
import { useForm } from 'react-hook-form';
import { useAppDispatch, useAppSelector } from '@store/index';
import { login, register, clearError } from '@store/slices/authSlice';

interface LoginForm {
  email: string;
  password: string;
  name?: string;
}

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const dispatch = useAppDispatch();
  const { isLoading, error, isAuthenticated } = useAppSelector((state) => state.auth);
  const [isRegisterMode, setIsRegisterMode] = useState(false);

  const {
    register: registerField,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginForm>();

  if (isAuthenticated) {
    return <Navigate to="/" replace />;
  }

  const onSubmit = async (data: LoginForm) => {
    dispatch(clearError());
    
    try {
      if (isRegisterMode) {
        await dispatch(register({
          email: data.email,
          password: data.password,
          name: data.name || data.email.split('@')[0],
        })).unwrap();
      } else {
        await dispatch(login({
          email: data.email,
          password: data.password,
        })).unwrap();
      }
      navigate('/');
    } catch (err) {
      // Error is handled by the Redux slice
    }
  };

  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        bgcolor: 'background.default',
      }}
    >
      <Paper
        elevation={3}
        sx={{
          p: 4,
          width: '100%',
          maxWidth: 400,
        }}
      >
        <Typography variant="h4" component="h1" align="center" gutterBottom>
          {isRegisterMode ? 'Create Account' : 'Login'}
        </Typography>
        
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <form onSubmit={handleSubmit(onSubmit)}>
          {isRegisterMode && (
            <TextField
              fullWidth
              label="Name"
              margin="normal"
              {...registerField('name')}
              error={!!errors.name}
              helperText={errors.name?.message}
            />
          )}
          
          <TextField
            fullWidth
            label="Email"
            type="email"
            margin="normal"
            {...registerField('email', {
              required: 'Email is required',
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: 'Invalid email address',
              },
            })}
            error={!!errors.email}
            helperText={errors.email?.message}
          />
          
          <TextField
            fullWidth
            label="Password"
            type="password"
            margin="normal"
            {...registerField('password', {
              required: 'Password is required',
              minLength: {
                value: 6,
                message: 'Password must be at least 6 characters',
              },
            })}
            error={!!errors.password}
            helperText={errors.password?.message}
          />

          <Button
            fullWidth
            type="submit"
            variant="contained"
            size="large"
            sx={{ mt: 3, mb: 2 }}
            disabled={isLoading}
          >
            {isLoading ? (
              <CircularProgress size={24} />
            ) : isRegisterMode ? (
              'Register'
            ) : (
              'Login'
            )}
          </Button>

          <Box sx={{ textAlign: 'center' }}>
            <Typography variant="body2">
              {isRegisterMode ? 'Already have an account?' : "Don't have an account?"}{' '}
              <Link
                component="button"
                variant="body2"
                onClick={(e) => {
                  e.preventDefault();
                  setIsRegisterMode(!isRegisterMode);
                  dispatch(clearError());
                }}
              >
                {isRegisterMode ? 'Login' : 'Register'}
              </Link>
            </Typography>
          </Box>
        </form>
      </Paper>
    </Box>
  );
};

export default LoginPage;