import React, { useState } from 'react';
import TodoList from './TodoList';
import Navbar from '../components/Navbar';  // Impor Navbar

const TodoPage = () => {
  const [todoList, setTodoList] = useState([
    // Contoh data tugas
    { id: 1, title: 'Mengerjakan Proyek', description: 'Buat proyek React', priority: 'High', dueDate: '2023-12-31' },
    // Tambahkan tugas lainnya sesuai kebutuhan
  ]);

  const handleEdit = (taskId) => {
    // Logika untuk menangani pengeditan tugas
    console.log('Edit task dengan ID:', taskId);
  };

  const handleDelete = (taskId) => {
    // Logika untuk menangani penghapusan tugas
    console.log('Delete task dengan ID:', taskId);
  };

  const handleLogout = () => {
    // Logika untuk logout (sesuaikan dengan kebutuhan aplikasi Anda)
    console.log('Logout');
  };

  return (
    <div>
      {/* Panggil Navbar dan berikan prop onLogout */}
      <Navbar onLogout={handleLogout} />

      <h1>Todo List</h1>
      <TodoList todoList={todoList} onEdit={handleEdit} onDelete={handleDelete} />
    </div>
  );
};

export default TodoPage;
