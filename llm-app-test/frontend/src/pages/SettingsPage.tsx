import { Typography } from '@mui/material';

const SettingsPage: React.FC = () => {
  return (
    <div>
      <Typography variant="h4" component="h1" gutterBottom>
        Settings
      </Typography>
      <Typography variant="body1" color="text.secondary">
        Settings and API key management will be implemented here
      </Typography>
    </div>
  );
};

export default SettingsPage;