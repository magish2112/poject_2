import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Typography } from '@mui/material';

export default function HomePage() {
  const navigate = useNavigate();

  return (
    <Box sx={{ textAlign: 'center', mt: 10 }}>
      <Typography variant="h3" gutterBottom>Добро пожаловать!</Typography>
      <Button
        variant="contained"
        color="primary"
        sx={{ m: 2, width: 250, height: 60, fontSize: 20 }}
        onClick={() => navigate('/login?role=doctor')}
      >
        Вход для врача
      </Button>
      <Button
        variant="contained"
        color="secondary"
        sx={{ m: 2, width: 250, height: 60, fontSize: 20 }}
        onClick={() => navigate('/login?role=patient')}
      >
        Вход для пациента
      </Button>
    </Box>
  );
}
