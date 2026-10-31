import api from './api';
import AsyncStorage from '@react-native-async-storage/async-storage';

export const loginUser = async (phone_number: string, password: string) => {
  const response = await api.post('/auth/token/', {
    username: phone_number, // Ou le champ configuré pour la connexion
    password,
  });

  if (response.data.access) {
    await AsyncStorage.setItem('access_token', response.data.access);
    await AsyncStorage.setItem('refresh_token', response.data.refresh);
  }
  return response.data;
};

export const logoutUser = async () => {
  await AsyncStorage.removeItem('access_token');
  await AsyncStorage.removeItem('refresh_token');
};

export const getCurrentUserProfile = async () => {
  const response = await api.get('/auth/me/');
  return response.data;
};