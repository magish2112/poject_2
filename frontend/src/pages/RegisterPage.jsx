import React from 'react';
import RegisterForm from '../components/RegisterForm';
import { useNavigate, useLocation } from 'react-router-dom';

export default function RegisterPage() {
  const navigate = useNavigate();
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const role = params.get('role') || 'doctor';

  // Только для врача!
  if (role !== 'doctor') {
    navigate('/login?role=patient');
    return null;
  }

  return <RegisterForm defaultRole="doctor" onSuccess={() => navigate('/login?role=doctor')} />;
} 