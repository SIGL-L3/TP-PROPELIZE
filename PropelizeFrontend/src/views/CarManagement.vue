<script lang="ts">
import { defineComponent } from 'vue'
import Car from '@/components/Car.vue'
import  axios from 'axios'
import Deletepopup from "@/components/icons/Deletepopup.vue";

export default defineComponent({
  name: 'Home',
  components: {
    Deletepopup,
    Car
  },
  data() {
    return {
      cars:[] as any [],
      carsdisplay:[] as any [],
      cartocreate:{
        registration_number: "",
        make:"",
        model:"",
        year:'',
        rentalprice:''
      },
      search_registration:String,
      search_price:Number
    }
  },
  mounted(): any {
    this.loaddata();
    this.search_registration=''
  },
  methods:{
    async loaddata(){
      try{
        const token = localStorage.getItem('access')
        if (token){
          const response = await axios.get('http://127.0.0.1:8000/api/get/',
              {
                headers: {
                  Authorization: `Bearer ${token}`
                }
              }
          )
          this.cars = response.data
          this.carsdisplay=this.cars;
          // console.log(this.cars)
        }
        // console.log(token,'dfdkshfjh')
      }catch (error){
        console.log('erreur de chargement',error)
      }

    },

    updateloacle(payload){
      this.cars.forEach((car,i)=>{
        if (car.id===payload.id){
          this.cars[i]=payload
          this.carsdisplay=this.cars
        }
      })
    },

    deletelocale(id){
      this.cars = this.cars.filter((car)=>car.id!=id);
      this.carsdisplay=this.cars;
    },
    async create_vehicule(){
      try{
        const token = localStorage.getItem('access')
        const response = await axios.post('http://127.0.0.1:8000/api/create/',this.cartocreate,{
          headers:{
            Authorization:`Bearer ${token}`,
            'Content-Type':'application/json'
          }
        })
        if (response.status===201){
          this.cars.push(response.data)
          this.carsdisplay=this.cars
          this.cartocreate= {registration_number: "", make: "", model: "", year: '', rentalprice: ''}
          console.log('cree')
          }
        }catch (e) {
        console.log(e)
      }
    },

    searchByRegistration(e){
      this.carsdisplay=this.cars.filter(car=>{
        const tmp = e.target.value.trim().toLowerCase()
        return car.registration_number.toLowerCase().includes(tmp)
      })
    },

    searchByMaxPrice() {
      if (Number(this.search_price)>0){
        this.carsdisplay = this.cars.filter(car => {
          return car.rentalprice <= Number(this.search_price)
        })
      }else{
        this.carsdisplay=this.cars
      }
    },

    logout(){}
  }
})
</script>

<template>
  <div>
    <div class="car-container">
      <nav>

        <div class="nav-left">
          propelize
        </div>
        <div class="nav-right">
          <input type="text" placeholder="registration number" v-model="search_registration" @keyup="searchByRegistration">
<!--          <i class='bx  bx-search bx-sm'  style='color:#ffffff;cursor: pointer' @click="searchByRegistration"></i>-->
          <form @submit.prevent="searchByMaxPrice">
            <input type="number" min="0" placeholder="max price" v-model="search_price">
            <i class='bx  bx-search bx-sm'  style='color:#ffffff;cursor: pointer' @click="searchByMaxPrice" ></i>
          </form>
          <p style="color: red; cursor: pointer" @click="logout">logout</p>
        </div>
      </nav>
      <div class="left">
        <form @submit.prevent="create_vehicule">
          <input type="text" placeholder="registration_number" v-model="cartocreate.registration_number" required autofocus>
          <input type="text" placeholder="make" v-model="cartocreate.make" required>
          <input type="text" placeholder="model" v-model="cartocreate.model" required>
          <input type="number" min="0" placeholder="year" v-model="cartocreate.year" required>
          <input type="number" min="0" maxlength="13" placeholder="rental price" v-model="cartocreate.rentalprice" required>
          <button>+</button>
        </form>
      </div>
      <div class="right">
        <h1>Vehicules : </h1>
        <div class="cars">
          <div v-for="car in carsdisplay">
            <Car
                @updateloacle="updateloacle"
                @deletelocale="deletelocale"
                :id="car.id"
                :registration_number="car.registration_number"
                :make="car.make"
                :model="car.model"
                :year="car.year"
                :rentalprice="car.rentalprice"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>

  .car-container{
    display: flex;
  }

  nav{
    position: absolute;
    top: 0;
    left: 0;
    background: #202020;
    width: 100%;
    height: 60px;

    display: flex;
    align-items: center;
    gap: 20px;
  }

  .nav-left{
    width: 40%;

    font-weight: bolder;
    letter-spacing: 20px;
    display: flex;
    align-items: center;
    justify-content: center;

  }

  .nav-right{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;

    width: 60%;
  }

  .nav-right input{
    border: none;
    height: 30px;
    padding: 10px;
    outline: none;
    border-radius: 10px;
  }

  .right h1{
    margin-top: 80px;
    margin-left: 40px;
    color: #181818;
    font-weight: bolder;
  }

  .left{
    height: 100vh;
    width: 40%;
    background: url("../assets/images/backgound.png");
    background-size: cover;
  }

  .left form{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    gap: 1rem;
  }

  .left input{
    height: 2rem;
    width: 45%;
    border: 1px solid rgba(255, 255, 255, 0.84);
    border-radius: 5px;
    padding-left: 20px;
    background: rgba(255, 255, 255, 0.17);
    color: white;
    font-size: .8rem;
  }

  .left input:focus{
    transform: scale(1.02);
  }

  .left button{
    height: 2rem;
    width: 45%;
    border: none;
    border-radius: 5px;
    padding-left: 20px;
    background: rgba(255, 255, 255, 0.17);
    color: white;

    font-weight: bold;
    font-size: 1.5rem;

    cursor: pointer;
    background: #DA0000;
  }

  .right{
    height: 100vh;
    width: 60%;
    background: #f3f3f3;
  }


  .right{
    overflow: scroll;
  }
  .cars{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 1.5rem;
    padding: 0 40px;
    margin-top: 20px;
  }

  .nav-right form{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
  }
</style>