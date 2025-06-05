import { Typography } from '@mui/material';

const DashboardPage: React.FC = () => {
  return (
    <div>
      <Typography variant="h4" component="h1" gutterBottom>
        Dashboard
      </Typography>
      <Typography variant="body1" color="text.secondary">
        Analytics dashboard will be implemented here
      </Typography>
    </div>
  );
};

export default DashboardPage;