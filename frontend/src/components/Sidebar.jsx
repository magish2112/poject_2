import React, { useContext } from 'react';
import { Drawer, List, ListItemButton, ListItemText } from '@mui/material';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

export default function Sidebar() {
  const { user } = useContext(AuthContext);
  return (
    <Drawer
      variant="permanent"
      sx={{
        width: 200,
        flexShrink: 0,
        [`& .MuiDrawer-paper`]: { width: 200, boxSizing: 'border-box', background: '#f5f5f5', mt: '64px' },
      }}
    >
      <List>
        <ListItemButton component={Link} to="/plans">
          <ListItemText primary="Планы" />
        </ListItemButton>
        <ListItemButton component={Link} to="/patients">
          <ListItemText primary="Пациенты" />
        </ListItemButton>
        <ListItemButton component={Link} to="/catalog">
          <ListItemText primary="Каталог" />
        </ListItemButton>
        {user?.role === 'admin' && (
          <ListItemButton component={Link} to="/admin">
            <ListItemText primary="Админ-панель" />
          </ListItemButton>
        )}
      </List>
    </Drawer>
  );
}