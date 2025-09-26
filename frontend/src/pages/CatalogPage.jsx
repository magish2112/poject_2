import React, { useEffect, useState, useContext } from 'react';
import { getCatalog } from '../api/catalog';
import { AuthContext } from '../context/AuthContext';
import CatalogList from '../components/CatalogList';
import { Box, Typography } from '@mui/material';

export default function CatalogPage() {
  const { token } = useContext(AuthContext);
  const [items, setItems] = useState([]);

  useEffect(() => {
    if (!token) return;
    getCatalog(token).then(res => setItems(res.data));
    // eslint-disable-next-line
  }, [token]);

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" sx={{ mb: 2 }}>Каталог</Typography>
      <CatalogList items={items} />
    </Box>
  );
} 