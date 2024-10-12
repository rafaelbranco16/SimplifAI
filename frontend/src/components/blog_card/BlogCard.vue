<template>
    <div class="blog-card-container">
      <router-link to="/entry-note" class="blog-card">
        <h2>Nota de Entrada</h2>
        <p>Descrição da nota de entrada. Clique aqui para saber mais.</p>
      </router-link>
  
      <router-link to="/upload-audio" class="blog-card">
        <h2>Diário Clínico</h2>
        <p>Descrição do diário clínico. Clique aqui para saber mais.</p>
      </router-link>
  
      <router-link to="/discharge-note" class="blog-card">
        <h2>Nota de Alta</h2>
        <p>Descrição da nota de alta. Clique aqui para saber mais.</p>
      </router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'BlogCard',
  }
  </script>
  
  <style scoped>
  .blog-card-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 2rem 0;
  }
  
  .blog-card {
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    width: 250px;
    text-decoration: none;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .blog-card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }
  
  .blog-card h2 {
    color: #333;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }
  
  .blog-card p {
    color: #666;
    font-size: 1rem;
  }
  </style>
  