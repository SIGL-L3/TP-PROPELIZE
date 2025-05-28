import { createRouter, createWebHistory } from 'vue-router'
import SignIn from "@/views/Sign-in.vue";
import SignUp from "@/views/Sign-up.vue";
import CarManagement from "@/views/CarManagement.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'CarManagement',
      component: CarManagement,
    },

    {
      path: '/sign-in',
      name: 'sign-in',
      component: SignIn,
    },

    {
      path: '/sign-up',
      name: 'signup',
      component:SignUp,
    },
  ],
})

export default router
