import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const registerUser = (data) =>
  axios.post(`${API_URL}/auth/register`, data);

export const loginUser = (data) =>
  axios.post(`${API_URL}/auth/login`, data);

// Changed endpoint from "/users/me" to "/auth/me"
export const getCurrentUser = (token) =>
  axios.get(`${API_URL}/auth/me`, {
    headers: { Authorization: `Bearer ${token}` }
  });