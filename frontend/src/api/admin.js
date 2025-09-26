import axios from 'axios';

export const getUsers = (token) =>
  axios.get('http://localhost:8000/admin/users', { headers: { Authorization: `Bearer ${token}` } });

export const changeUserRole = (userId, role, token) =>
  axios.patch(`http://localhost:8000/admin/users/${userId}/role?role=${role}`, {}, { headers: { Authorization: `Bearer ${token}` } });

export const deleteUser = (userId, token) =>
  axios.delete(`http://localhost:8000/admin/users/${userId}`, { headers: { Authorization: `Bearer ${token}` } });
