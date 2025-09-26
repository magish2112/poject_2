import React, { useState, useContext } from 'react';
import { loginUser } from '../api/auth';
import { AuthContext } from '../context/AuthContext';
import { Box, Button, TextField, Typography, Alert } from '@mui/material';

export default function LoginForm({ defaultRole = 'patient', onSuccess }) {
  const [form, setForm] = useState({
    email: '',
    password: '',
    role: defaultRole,
  });
  const [error, setError] = useState('');
  const { login } = useContext(AuthContext);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    try {
      const res = await loginUser({ email: form.email, password: form.password });
      const token = res.data.access_token;
      await login(token);
      if (onSuccess) onSuccess();
    } catch (err) {
      let errorMessage = err.response?.data?.detail || 'Ошибка входа';
      if (typeof errorMessage === 'object') {
        errorMessage = JSON.stringify(errorMessage);
      }
      setError(errorMessage);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ maxWidth: 400, mx: 'auto', mt: 8 }}>
      <Typography variant="h4" align="center" gutterBottom>Вход</Typography>
      <TextField
        label="Email"
        name="email"
        value={form.email}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required
      />
      <TextField
        label="Пароль"
        name="password"
        type="password"
        value={form.password}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required
      />
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
        Войти
      </Button>
      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
    </Box>
  );
}