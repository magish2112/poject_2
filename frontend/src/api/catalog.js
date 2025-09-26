import axios from 'axios';

const API_URL = 'http://localhost:8000';

export async function getCatalog(token) {
  return axios.get(`${API_URL}/catalog/`, {
    headers: { Authorization: `Bearer ${token}` }
  });
} 