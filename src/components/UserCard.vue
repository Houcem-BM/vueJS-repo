<template>
    <div class="user-card">
      <h3>{{ name }}</h3>
      <p>Email: {{ email }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ['name', 'email'],
  };
  </script>
  
  <style>
  .user-card {
    border: 1px solid #ddd;
    padding: 10px;
    margin-bottom: 10px;
  }
  </style>
  