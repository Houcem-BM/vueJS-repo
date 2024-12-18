<template>
    <div>
      <h1>Our Users</h1>
      <UserCard name="John Doe" email="john.doe@example.com" />
      <UserCard name="Jane Smith" email="jane.smith@example.com" />
    </div>
  </template>
  
  <script>
  import UserCard from '../components/UserCard-comp.vue';
  
  export default {
    components: {
      UserCard,
    },
  };
  </script>
  