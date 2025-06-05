import { useNavigate } from 'react-router-dom';
import { Button, Typography, Box, Paper, Grid } from '@mui/material';
import {
  Chat as ChatIcon,
  Dashboard as DashboardIcon,
  Science as ScienceIcon,
} from '@mui/icons-material';

const HomePage: React.FC = () => {
  const navigate = useNavigate();

  const features = [
    {
      title: 'Multi-LLM Chat',
      description: 'Compare responses from OpenAI, Google, and Anthropic simultaneously',
      icon: <ChatIcon fontSize="large" />,
      action: () => navigate('/chat'),
    },
    {
      title: 'Analytics Dashboard',
      description: 'Track usage, costs, and performance metrics across all providers',
      icon: <DashboardIcon fontSize="large" />,
      action: () => navigate('/dashboard'),
    },
    {
      title: 'Evaluation System',
      description: 'Rate and analyze LLM responses to find the best model for your needs',
      icon: <ScienceIcon fontSize="large" />,
      action: () => navigate('/chat'),
    },
  ];

  return (
    <Box>
      <Typography variant="h3" component="h1" gutterBottom>
        Welcome to LLM Chat Platform
      </Typography>
      <Typography variant="h6" color="text.secondary" paragraph>
        Compare and evaluate multiple AI language models in one unified interface
      </Typography>

      <Grid container spacing={3} sx={{ mt: 2 }}>
        {features.map((feature, index) => (
          <Grid item xs={12} md={4} key={index}>
            <Paper
              sx={{
                p: 3,
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                textAlign: 'center',
                cursor: 'pointer',
                transition: 'transform 0.2s',
                '&:hover': {
                  transform: 'translateY(-4px)',
                },
              }}
              onClick={feature.action}
            >
              <Box sx={{ color: 'primary.main', mb: 2 }}>{feature.icon}</Box>
              <Typography variant="h5" component="h2" gutterBottom>
                {feature.title}
              </Typography>
              <Typography variant="body2" color="text.secondary" sx={{ flexGrow: 1 }}>
                {feature.description}
              </Typography>
              <Button variant="contained" sx={{ mt: 2 }} onClick={feature.action}>
                Get Started
              </Button>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default HomePage;