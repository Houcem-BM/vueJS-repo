<template>
    <div>
      <h1>Our Users</h1>
      <appUserCard name="John Doe" email="john.doe@example.com" />
      <appUserCard name="Jane Smith" email="jane.smith@example.com" />
    </div>
  </template>
  
  <script>
  import appUserCard from '../components/appUserCard.vue';
  
  export default {
    components: {
      appUserCard,
    },
  };
  </script>
  