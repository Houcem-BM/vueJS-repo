import { createRouter, createWebHistory } from 'vue-router';
import SignUp from './pages/SignUp.vue';
import LoginPage from './pages/LoginPage.vue';
import Home from './pages/Home.vue';
import update from './pages/updatePage.vue';
import Add from './pages/AddPage.vue';

const routes = [
  { 
    name:'SignUp',
    path: '/signup',
    component: SignUp

  },
  { 
    name:'Login',
    path: '/Login',
    component: LoginPage 
  },
  { 
    name:'Home',
    path: '/',
    component: Home 
  },
  { 
    name:'update',
    path: '/update/:id',
    component: update
  },
  { 
    name:'Add',
    path: '/add',
    component: Add
  }
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;