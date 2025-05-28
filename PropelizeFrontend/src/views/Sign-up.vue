<script setup lang="ts">
import { ref } from 'vue'
import {useRouter} from "vue-router";
import axios from 'axios'


const username = ref('')
const password = ref('')
const errorsDisplay = ref<boolean>()
const router = useRouter()


const handleregister = async () => {

  try{
    const response = await axios.post('http://127.0.0.1:8000/user/create/',{
      name: username.value,
      password: password.value,
    })
    if (response.status === 201) {
      router.push('/sign-in')
      console.log(response.data)
    }else{
      console.log(response.data)
    }

  }catch(err){
    if(err.response.status === 400){
      console.log(err.response.data)
      errorsDisplay.value = true
    }
  }

}

</script>

<template>
  <div class="container">
    <div class="subcontainer">
      <form @submit.prevent="handleregister">
        <div>
          <p>Welcome To Propelize</p>
          <h5>Create your account</h5>
        </div>
        <i class='bx  bxs-user bx-sm'  style='color:#ffffff'></i>
        <i class='bx  bxs-lock bx-sm'  style='color:#ffffff'></i>
        <div class="fields">
          <p class="error" v-if="errorsDisplay">username already take</p>
          <input type="text" placeholder="username" v-model="username" autofocus required>
          <input type="password" placeholder="password" v-model="password" autocomplete="off" required>
          <button style="background: #DA0000">Sign up</button>
        </div>
        <h5>Already have an account ? <span @click="router.push('sign-in')">Sign in</span></h5>
      </form>
      <div class="cars_image">
        <h5>Another way to manage your vehicule</h5>
        <div>
          <img src="../assets/images/car.png">
          <img src="../assets/images/car.png">
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.cars_image{
  position: relative;
  top: 0;
  left: 0;
}

.container form{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;

  width:40%;
  height: auto;

  padding: 50px 0;
  background: rgba(0, 0, 0, 0.19);
  border-radius: 25px;
  border: 1px solid rgba(255, 255, 255, 0.22);

  position: relative;
  left: -80px;
  z-index: 1;

  backdrop-filter: blur(60px) brightness(1.1);
}


.container form .fields{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  gap: 2rem;
}

.container form .fields input{
  border: 2px #ffffff solid;
  padding: 7px;
  border-radius: 10px;

  width: 300px;
  height: 45px;
  background: rgba(255, 255, 255, 0.3);
  color: white;

  padding-left: 20px;
}

.container form .fields button{
  height: 2rem;
  width: 45%;
  border: none;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.17);
  color: white;

  font-weight: bold;

  cursor: pointer;
  background: #DA0000;
}

span{
  color: #DA0000;
  cursor: pointer;
}

.container form .fields input::placeholder{
  color: rgba(255, 255, 255, 0.39);
}


.subcontainer{
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
  justify-content: center;

  width: 70% ;
}
.subcontainer div:first-child{
  display: flex;
  align-items: center;
  flex-direction: column;
}

.subcontainer p{
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
}

.subcontainer .cars_image h5{

  color: rgba(255, 255, 255, 0.75);
}

.subcontainer h5{
  font-weight: normal;
  font-size: 0.8rem;
}

.container{
  display: flex;
  align-items: center;
  justify-content: center;

  height: 100vh;
}

.cars_image h5{
  position: absolute;
  bottom: 20px;
  left: 20px;
}

.subcontainer h5:last-child{
  margin-top: 20px;
}

.bxs-user{
  position: relative;
  left: 120px;
  top: 60px;
}

.bxs-lock{
  position: relative;
  left: 120px;
  top: 110px;
}

.cars_image div img{
  width: 100%;
  height: auto;
}

.cars_image img:first-child{
  position: absolute;
  top: 0;
  left: 0;
  filter: blur(80px);
  z-index: -1;

}
</style>