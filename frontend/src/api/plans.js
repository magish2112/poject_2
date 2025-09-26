import axios from 'axios';

const API_URL = 'http://localhost:8000';

export async function getPlans(token) {
  return axios.get(`${API_URL}/plans/`, {
    headers: { Authorization: `Bearer ${token}` }
  });
}

export async function createPlan(data, token) {
  return axios.post(`${API_URL}/plans/`, data, {
    headers: { Authorization: `Bearer ${token}` }
  });
}

export async function updatePlan(id, data, token) {
  return axios.put(`${API_URL}/plans/${id}`, data, {
    headers: { Authorization: `Bearer ${token}` }
  });
}

export async function deletePlan(id, token) {
  return axios.delete(`${API_URL}/plans/${id}`, {
    headers: { Authorization: `Bearer ${token}` }
  });
} 