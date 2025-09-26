import React from 'react';

export default function UserList({ users, onRoleChange, onDelete }) {
  return (
    <table style={{ width: '100%', marginTop: '1rem', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Email</th>
          <th>Имя</th>
          <th>Фамилия</th>
          <th>Роль</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        {users.map(u => (
          <tr key={u.id}>
            <td>{u.id}</td>
            <td>{u.email}</td>
            <td>{u.first_name}</td>
            <td>{u.last_name}</td>
            <td>
              <select value={u.role} onChange={e => onRoleChange(u.id, e.target.value)}>
                <option value="admin">admin</option>
                <option value="doctor">doctor</option>
                <option value="patient">patient</option>
              </select>
            </td>
            <td>
              <button onClick={() => onDelete(u.id)}>Удалить</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
