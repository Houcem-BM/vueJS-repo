<template>
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/about">About</router-link></li>
          <li><router-link to="/users">Users</router-link></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <style>
  header {
    background-color: #333;
    color: white;
    padding: 10px;
  }
  nav ul {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
  }
  nav ul li {
    margin-right: 20px;
  }
  nav ul li a {
    color: white;
    text-decoration: none;
  }
  </style>
  