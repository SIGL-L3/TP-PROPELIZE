<script lang="ts">
import { defineComponent } from 'vue'
import CarDetails from "@/components/CarDetails.vue";
import axios from "axios";
import Deletepopup from "@/components/icons/Deletepopup.vue";

export default defineComponent({
  name: 'Car',
  components: {Deletepopup, CarDetails},
  props:{
    id:{
      type:Number,
    },
    registration_number:{
      type:String,
    },
    make:{
      type:String,
    },
    model:{
      type:String,
    },
    year:{
      type:Number,
    },
    rentalprice:{
      type:Number,
    }
  },
  data() {
    return {
      showupdate:false,
      showdelete:false
    }
  },

  methods:{
    closeupdate(){
      this.showupdate=false
    },
    updateloacle(payload){
      this.$emit('updateloacle',payload)
    },

    async deletecar(id){
      try {
        const token = localStorage.getItem('access')
        const response = await axios.delete(`http://127.0.0.1:8000/api/delete/${id}/`,{
          headers:{
            Authorization:`Bearer ${token}`,
            'Content-Type':'application/json'
          }
        })
        if(response.status===204){
          this.$emit('deletelocale',id)
          console.log('deleted')
        }
      }catch (e) {
        console.log(e)
      }
    }
  }

})
</script>

<template>
  <CarDetails v-if="showupdate" @closeupdate="closeupdate" @updateloacle="updateloacle"
      :id="id"
      :registration_number="registration_number"
      :make="make"
      :model="model"
      :year="year"
      :rentalprice="rentalprice"
  />
  <Deletepopup @deletecar="deletecar" @closeDeltePopoUp="showdelete=false" v-if="showdelete"
      :id="id"
      :registration_number="registration_number"
      :make="make"
      :model="model"
      :year="year"
      :rentalprice="rentalprice"
  ></Deletepopup>
  <div class="car">
    <div class="top">
      <p style="color: #a3a3a3">{{registration_number}}</p>
      <p>{{ make }}</p>
      <p>{{ model }}</p>
      <p>{{ year }}</p>
    </div>

    <div class="bottom">
      <p>{{ rentalprice }} $</p>
      <div class="icon">
        <div @click="showupdate=true">
          <img src="../assets/images/edit.png" width="20px">
        </div>
        <div @click="showdelete=true">
          <img src="../assets/images/bin.png" width="20px">
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
  .car{
    width: 160px;
    background: #ffffff;
    border-radius: 7px;
    color: #181818;
    overflow: hidden;
  }
  .car .bottom{
    display: flex;
    align-content: center;
    padding: 0;
  }

  .car .bottom p{
    text-align: center;
    width: 70%;
  }

  .car .bottom .icon{
    display: flex;
    width: 40%;
    justify-content: space-around;
    background: #2c3e50;
  }

  .car .top{
    padding: 10px;
  }


  .car .bottom p{
    background: #181818;
    color: white;
    font-weight: bold;
  }


  .car .bottom .icon div:first-child{
    background: #84A200;
    width: 50%;

    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .car .bottom .icon div:last-child{
    background: #D30000;
    width: 50%;

    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .top p{
    font-weight: bold;
  }
</style>