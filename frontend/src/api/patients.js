import axios from 'axios';

const API_URL = 'http://localhost:8000';

export async function getPatients(token) {
  return axios.get(`${API_URL}/patients/`, {
    headers: { Authorization: `Bearer ${token}` }
  });
}

export async function createPatient(data, token) {
  return axios.post(`${API_URL}/patients/`, data, {
    headers: { Authorization: `Bearer ${token}` }
  });
}

export async function updatePatient(id, data, token) {
  return axios.put(`${API_URL}/patients/${id}`, data, {
    headers: { Authorization: `Bearer ${token}` }
  });
}

export async function deletePatient(id, token) {
  return axios.delete(`${API_URL}/patients/${id}`, {
    headers: { Authorization: `Bearer ${token}` }
  });
} 