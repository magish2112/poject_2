import React, { useEffect, useState, useContext } from 'react';
import { getPlans, createPlan, updatePlan, deletePlan } from '../api/plans';
import { AuthContext } from '../context/AuthContext';
import PlanList from '../components/PlanList';
import PlanForm from '../components/PlanForm';
import { Box, Button, Dialog, DialogContent, DialogTitle } from '@mui/material';

export default function PlansPage() {
  const { token } = useContext(AuthContext);
  const [plans, setPlans] = useState([]);
  const [editing, setEditing] = useState(null);
  const [open, setOpen] = useState(false);

  const fetchPlans = async () => {
    if (!token) return;
    const res = await getPlans(token);
    setPlans(res.data);
  };

  useEffect(() => {
    fetchPlans();
    // eslint-disable-next-line
  }, [token]);

  const handleCreate = () => {
    setEditing(null);
    setOpen(true);
  };

  const handleEdit = (plan) => {
    setEditing(plan);
    setOpen(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Удалить план?')) return;
    await deletePlan(id, token);
    fetchPlans();
  };

  const handleSave = async (data) => {
    if (editing) {
      await updatePlan(editing.id, data, token);
    } else {
      await createPlan({
        ...data,
        patient_id: Number(data.patient_id)
      }, token);
    }
    setOpen(false);
    fetchPlans();
  };

  return (
    <Box sx={{ p: 3 }}>
      <Button variant="contained" color="primary" onClick={handleCreate} sx={{ mb: 2 }}>
        Создать план
      </Button>
      <PlanList plans={plans} onEdit={handleEdit} onDelete={handleDelete} />
      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>{editing ? 'Редактировать план' : 'Создать план'}</DialogTitle>
        <DialogContent>
          <PlanForm initial={editing} onSave={handleSave} onCancel={() => setOpen(false)} />
        </DialogContent>
      </Dialog>
    </Box>
  );
} 