import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = () => {
    // Lakukan logika autentikasi di sini
    console.log('Login dengan:', username, password);

    // Redirect ke halaman todo setelah login berhasil
    navigate('/todo');
  };

  return (
    <div style={{ maxWidth: '300px', margin: 'auto', marginTop: '50px', textAlign: 'center' }}>
      <h1>TODO APP</h1>
      <TextField
        label="Username"
        variant="outlined"
        fullWidth
        margin="normal"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <TextField
        label="Password"
        variant="outlined"
        type="password"
        fullWidth
        margin="normal"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <Button variant="contained" color="primary" fullWidth onClick={handleLogin}>
        Login
      </Button>
      <p style={{ textAlign: 'center', marginTop: '10px' }}>
        <Link to="/register">Register</Link> | <Link to="/forget-password">Lupa Password</Link>
      </p>
    </div>
  );
};

export default LoginForm;
