import React, { useState } from 'react';
import { Box, Button, TextField } from '@mui/material';

export default function PatientForm({ initial, onSave, onCancel }) {
  const [form, setForm] = useState(initial || {
    first_name: '',
    last_name: '',
    email: '',
    // другие поля по необходимости
  });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    onSave(form);
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
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
        label="Email"
        name="email"
        type="email"
        value={form.email}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required
      />
      {/* другие поля */}
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
        <Button onClick={onCancel} sx={{ mr: 2 }}>Отмена</Button>
        <Button type="submit" variant="contained" color="primary">Сохранить</Button>
      </Box>
    </Box>
  );
} 