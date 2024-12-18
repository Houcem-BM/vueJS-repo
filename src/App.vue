<template>
  <div>
    <Header />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header-comp.vue';
import Footer from './components/Footer-comp.vue';

export default {
  components: {
    Header,
    Footer,
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
main {
  padding: 20px;
}
</style>
