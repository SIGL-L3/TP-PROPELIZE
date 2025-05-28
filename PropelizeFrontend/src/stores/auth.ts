import {defineStore} from "pinia";
import axios from 'axios'

export  const useAuthStore = defineStore('auth', {
    state:()=>({
        access:localStorage.getItem("access") || '',
        refresh:localStorage.getItem("refresh") || '',
    }),
    actions:{
        async login(username:string,password:string){
            try{
                const response = await axios.post('http://127.0.0.1:8000/user/login/',{
                    name:username,
                    password:password
                })
                this.access = response.data.access;
                this.refresh = response.data.refresh;
                localStorage.setItem('access', response.data.access);
                localStorage.setItem('refresh', response.data.refresh);
                return true;
            }catch (error){
                console.log('login failed',error);
                return false;
            }
        },
        logout(){
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            this.access = '';
            this.refresh = '';
        }
    }
})