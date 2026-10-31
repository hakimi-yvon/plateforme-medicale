import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Alert } from 'react-native';
import { loginUser, getCurrentUserProfile } from './src/services/auth';

export default function App() {
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [user, setUser] = useState<any>(null);

  const handleLogin = async () => {
    try {
      await loginUser(phone, password);
      const profile = await getCurrentUserProfile();
      setUser(profile);
      Alert.alert('Succès', `Bienvenue ${profile.username}`);
    } catch (error: any) {
      Alert.alert('Erreur', 'Échec de la connexion. Vérifiez vos identifiants.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Plateforme Médicale</Text>

      {user ? (
        <View>
          <Text style={styles.text}>Connecté en tant que : {user.username}</Text>
          <Text style={styles.text}>Rôle : {user.role}</Text>
        </View>
      ) : (
        <View style={styles.form}>
          <TextInput
            style={styles.input}
            placeholder="Numéro de téléphone"
            value={phone}
            onChangeText={setPhone}
            keyboardType="phone-pad"
          />
          <TextInput
            style={styles.input}
            placeholder="Mot de passe"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
          />
          <TouchableOpacity style={styles.button} onPress={handleLogin}>
            <Text style={styles.buttonText}>Se connecter</Text>
          </TouchableOpacity>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.compile({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 30,
    color: '#0066cc',
  },
  form: {
    width: '100%',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 12,
    borderRadius: 8,
    marginBottom: 15,
  },
  button: {
    backgroundColor: '#0066cc',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  text: {
    fontSize: 16,
    marginBottom: 10,
  },
});