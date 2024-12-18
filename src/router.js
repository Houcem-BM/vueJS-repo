import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/appHome.vue';
import About from './pages/appAbout.vue';
import Users from './pages/appUsers.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/users', component: Users }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
