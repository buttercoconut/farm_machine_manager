
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '../views/Dashboard.vue';
import MachineManagement from '../views/MachineManagement.vue';
import RentalManagement from '../views/RentalManagement.vue';

const routes = [
  { path: '/', component: Dashboard },
  { path: '/machines', component: MachineManagement },
  { path: '/rentals', component: RentalManagement },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
