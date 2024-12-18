<template>
  <div>
    <appHeader />
    <main>
      <router-view />
    </main>
    <appFooter />
  </div>
</template>

<script>
import appHeader from './components/appHeader.vue';
import appFooter from './components/appFooter.vue';

export default {
  components: {
    appHeader,
    appFooter,
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
