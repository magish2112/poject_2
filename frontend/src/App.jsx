import React, { useContext } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider, AuthContext } from './context/AuthContext';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import PlansPage from './pages/PlansPage';
import PatientsPage from './pages/PatientsPage';
import CatalogPage from './pages/CatalogPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import NotFound from './pages/NotFound';
import HomePage from './pages/HomePage';
import AdminPage from './pages/AdminPage';

function AppRoutes() {
  const { user } = useContext(AuthContext);

  if (!user) {
    // Неавторизованный пользователь — только главная и логин/регистрация
    return (
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="*" element={<HomePage />} />
      </Routes>
    );
  }

  // Авторизованный пользователь — весь функционал
  return (
    <>
      <Navbar />
      <div style={{ display: 'flex' }}>
        <Sidebar />
        <div style={{ flex: 1 }}>
          <Routes>
            <Route path="/" element={<PlansPage />} />
            <Route path="/plans" element={<PlansPage />} />
            <Route path="/patients" element={<PatientsPage />} />
            <Route path="/catalog" element={<CatalogPage />} />
            <Route path="/admin" element={<AdminPage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </AuthProvider>
  );
} 