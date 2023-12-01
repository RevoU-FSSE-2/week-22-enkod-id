import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import ForgetPasswordForm from './components/ForgetPasswordForm';
import TodoPage from './components/TodoPage';
import AddTodo from './components/AddTodo';

const App = () => {
  return (
    <Router>
      <div>
        
        <main>
          <Routes>
            {/* Rute default: */}
            <Route path="/" element={<LoginForm />} />

            {/* Rute lainnya: */}
            <Route path="/login" element={<LoginForm />} />
            <Route path="/register" element={<RegisterForm />} />
            <Route path="/forget-password" element={<ForgetPasswordForm />} />
            <Route path="/todo" element={<TodoPage />} />
            <Route path="/todo/edit/1" element={<AddTodo />} />
            {/* Tambahkan rute lainnya sesuai kebutuhan */}
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
