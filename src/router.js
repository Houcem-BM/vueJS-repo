import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home.vue';
import About from './pages/About.vue';
import Users from './pages/Users.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/users', component: Users },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
