import React, { useEffect, useState, useContext } from 'react';
import { getPatients, createPatient, updatePatient, deletePatient } from '../api/patients';
import { AuthContext } from '../context/AuthContext';
import PatientList from '../components/PatientList';
import PatientForm from '../components/PatientForm';
import { Box, Button, Dialog, DialogContent, DialogTitle } from '@mui/material';

export default function PatientsPage() {
  const { token } = useContext(AuthContext);
  const [patients, setPatients] = useState([]);
  const [editing, setEditing] = useState(null);
  const [open, setOpen] = useState(false);

  const fetchPatients = async () => {
    if (!token) return;
    const res = await getPatients(token);
    setPatients(res.data);
  };

  useEffect(() => {
    fetchPatients();
    // eslint-disable-next-line
  }, [token]);

  const handleCreate = () => {
    setEditing(null);
    setOpen(true);
  };

  const handleEdit = (patient) => {
    setEditing(patient);
    setOpen(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Удалить пациента?')) return;
    await deletePatient(id, token);
    fetchPatients();
  };

  const handleSave = async (data) => {
    if (editing) {
      await updatePatient(editing.id, data, token);
    } else {
      await createPatient(data, token);
    }
    setOpen(false);
    fetchPatients();
  };

  return (
    <Box sx={{ p: 3 }}>
      <Button variant="contained" color="primary" onClick={handleCreate} sx={{ mb: 2 }}>
        Добавить пациента
      </Button>
      <PatientList patients={patients} onEdit={handleEdit} onDelete={handleDelete} />
      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>{editing ? 'Редактировать пациента' : 'Добавить пациента'}</DialogTitle>
        <DialogContent>
          <PatientForm initial={editing} onSave={handleSave} onCancel={() => setOpen(false)} />
        </DialogContent>
      </Dialog>
    </Box>
  );
} 