import React, { useEffect, useState, useContext } from 'react';
import { getUsers, changeUserRole, deleteUser } from '../api/admin';
import { AuthContext } from '../context/AuthContext';
import UserList from '../components/UserList';

export default function AdminPage() {
  const { token, user } = useContext(AuthContext);
  const [users, setUsers] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!token) return;
    getUsers(token)
      .then(res => setUsers(res.data))
      .catch(() => setError('Ошибка загрузки пользователей'));
  }, [token]);

  const handleRoleChange = (userId, newRole) => {
    changeUserRole(userId, newRole, token).then(() => {
      setUsers(users => users.map(u => u.id === userId ? { ...u, role: newRole } : u));
    });
  };

  const handleDelete = (userId) => {
    if (!window.confirm('Удалить пользователя?')) return;
    deleteUser(userId, token).then(() => {
      setUsers(users => users.filter(u => u.id !== userId));
    });
  };

  if (!user || user.role !== 'admin') {
    return <div>Доступ запрещён</div>;
  }

  return (
    <div style={{ padding: 24 }}>
      <h2>Пользователи</h2>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <UserList users={users} onRoleChange={handleRoleChange} onDelete={handleDelete} />
    </div>
  );
}
