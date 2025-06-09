import { createRouter, createWebHistory } from 'vue-router'
import SignIn from "@/views/Sign-in.vue";
import SignUp from "@/views/Sign-up.vue";
import Home from "@/views/Home.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/home', name: 'home', component: Home,meta:{requiresAuth:true}},
    {path: '/sign-in', name: 'sign-in', component: SignIn,meta:{requiresAuth: false}},
    {path: '/sign-up', name: 'signup', component:SignUp,meta:{requiresAuth: false}},
  ],
})

const isAuthenticated = ()=>{
  return !!localStorage.getItem('access');
}

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()){
    console.log('sj')
    next({name:'sign-in'})
  }else if(to.name=== 'sign-in' && isAuthenticated()){
    next({name:'home'})
  }else{
    next()
  }
});
export default router
