import React, { useState } from 'react';
import { registerUser } from '../api/auth';
import { Box, Button, TextField, Typography, Alert, MenuItem } from '@mui/material';

export default function RegisterForm({ defaultRole = 'doctor', onSuccess }) {
  const [form, setForm] = useState({
    email: '',
    password: '',
    role: defaultRole,
    first_name: '',
    last_name: '',
    specialization: '',
    phone: '',
    date_of_birth: '',
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    setSuccess(false);
    try {
      await registerUser({ ...form, role: defaultRole });
      setSuccess(true);
      if (onSuccess) onSuccess();
    } catch (err) {
      let errorMessage = err.response?.data?.detail || 'Ошибка регистрации';
      if (typeof errorMessage === 'object') {
        errorMessage = JSON.stringify(errorMessage);
      }
      setError(errorMessage);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ maxWidth: 400, mx: 'auto', mt: 8 }}>
      <Typography variant="h4" align="center" gutterBottom>Регистрация</Typography>
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
      <TextField
        label="Имя"
        name="first_name"
        value={form.first_name}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required
      />
      <TextField
        label="Фамилия"
        name="last_name"
        value={form.last_name}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required
      />
      <TextField
        label="Специализация"
        name="specialization"
        value={form.specialization || ''}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required={form.role === 'doctor'}
        style={{ display: form.role === 'doctor' ? 'block' : 'none' }}
      />
      <TextField
        label="Телефон"
        name="phone"
        value={form.phone || ''}
        onChange={handleChange}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Дата рождения"
        name="date_of_birth"
        type="date"
        value={form.date_of_birth || ''}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required={form.role === 'patient'}
        style={{ display: form.role === 'patient' ? 'block' : 'none' }}
        InputLabelProps={{ shrink: true }}
      />
      <TextField
        name="role"
        value={form.role}
        type="hidden"
        style={{ display: 'none' }}
        inputProps={{ readOnly: true }}
      />
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
        Зарегистрироваться
      </Button>
      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
      {success && <Alert severity="success" sx={{ mt: 2 }}>Регистрация успешна!</Alert>}
    </Box>
  );
}