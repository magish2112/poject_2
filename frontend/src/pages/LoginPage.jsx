import React from 'react';
import LoginForm from '../components/LoginForm';
import { useNavigate, useLocation } from 'react-router-dom';
import { Box, Link } from '@mui/material';

export default function LoginPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const role = params.get('role') || 'patient';

  return (
    <Box>
      <LoginForm defaultRole={role} onSuccess={() => navigate('/plans')} />
      {role === 'doctor' && (
        <Box sx={{ textAlign: 'center', mt: 2 }}>
          <Link href="/register?role=doctor" underline="hover">
            Зарегистрироваться как врач
          </Link>
        </Box>
      )}
    </Box>
  );
} 