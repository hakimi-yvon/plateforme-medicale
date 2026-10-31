import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// En développement avec Expo / Tunnel, remplacez par l'URL de votre serveur Django ou de votre tunnel
const API_BASE_URL = 'http://10.0.2.2:8000/api/v1'; // Utiliser l'IP locale de votre machine ou l'URL du tunnel

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Intercepteur pour injecter automatiquement le Token JWT (Bearer)
api.interceptors.request.use(
  async (config) => {
    const token = await AsyncStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api;