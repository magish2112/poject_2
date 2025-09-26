import React, { useState } from 'react';
import { Box, Button, TextField } from '@mui/material';
import Autocomplete from '@mui/material/Autocomplete';
import axios from 'axios';

export default function PlanForm({ initial, onSave, onCancel }) {
  const [form, setForm] = useState(initial || {
    name: '',
    patient_id: '',
    date: '',
    // другие поля по необходимости
  });
  const [patientOptions, setPatientOptions] = useState([]);
  const [patientInput, setPatientInput] = useState('');

  const fetchPatients = async (query) => {
    if (!query) return;
    try {
      const res = await axios.get(`http://localhost:8000/patients/search/?q=${encodeURIComponent(query)}`);
      setPatientOptions(res.data);
    } catch (e) {
      setPatientOptions([]);
    }
  };

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
        label="Название плана"
        name="name"
        value={form.name}
        onChange={handleChange}
        fullWidth
        margin="normal"
        required
      />
      <Autocomplete
        freeSolo
        options={patientOptions}
        getOptionLabel={(option) =>
          option.first_name + ' ' + option.last_name + ' (' + option.email + ')'
        }
        onInputChange={(event, newInputValue) => {
          setPatientInput(newInputValue);
          fetchPatients(newInputValue);
        }}
        onChange={(event, newValue) => {
          setForm({ ...form, patient_id: newValue ? newValue.id : null });
        }}
        renderInput={(params) => (
          <TextField
            {...params}
            label="Пациент"
            margin="normal"
            fullWidth
            required
            value={patientInput}
          />
        )}
      />
      <TextField
        label="Дата"
        name="date"
        type="date"
        value={form.date}
        onChange={handleChange}
        fullWidth
        margin="normal"
        InputLabelProps={{ shrink: true }}
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