import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';

export default function Navbar() {
  const { user, logout } = useContext(AuthContext);

  return (
    <AppBar position="static" sx={{ background: '#1976d2' }}>
      <Toolbar>
        <Typography variant="h6" component={Link} to="/" sx={{ color: 'white', textDecoration: 'none', flexGrow: 1 }}>
          Fullscript Clone
        </Typography>
        {user ? (
          <>
            <Typography sx={{ mr: 2 }}>{user.email}</Typography>
            <Button color="inherit" onClick={logout}>Выйти</Button>
          </>
        ) : (
          <Box>
            <Button color="inherit" component={Link} to="/login">Вход</Button>
            <Button color="inherit" component={Link} to="/register">Регистрация</Button>
          </Box>
        )}
      </Toolbar>
    </AppBar>
  );
} 