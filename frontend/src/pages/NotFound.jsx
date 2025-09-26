import React from 'react';
import { Box, Typography } from '@mui/material';

export default function NotFound() {
  return (
    <Box sx={{ textAlign: 'center', mt: 8 }}>
      <Typography variant="h3" color="error">Страница не найдена (404)</Typography>
    </Box>
  );
} 