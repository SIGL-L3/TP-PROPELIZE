<script lang="ts">
import { defineComponent } from 'vue'
import CarDetails from "@/components/CarDetails.vue";
import axios from "axios";
import Deletepopup from "@/components/Deletepopup.vue";

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
    <div class="title">
      <p>{{registration_number}}</p>
      <p>{{ make }}</p>
      <p>{{ model }}</p>
      <p style="background-color: #C2FFD4">{{ year }}</p>
      <p style="background-color: #FFFAC2">{{ rentalprice }} $</p>
    </div>
    <div class="icon">
      <div @click="showupdate=true">
        <img src="../assets/images/edit.png" width="20px">
      </div>
      <div @click="showdelete=true">
        <img src="../assets/images/bin.png" width="20px">
      </div>
    </div>
  </div>
</template>
<style scoped>
  .car{
    color: #181818;

    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
    gap: 30px;
    background-color: #ffffff;
    width: fit-content;

    border-radius: 10px;
    padding: 25px;
    width: 90%;
  }

  .car div{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    overflow-x: auto;
  }

  .car >div{
    margin: 0 20px;
  }

  .car .title{
    display: grid;
    grid-template-columns:1fr 1fr 1fr 1fr 1fr;

    width: 70%;
  }
  .title p{
    white-space: nowrap;
    background: #f8f8f8;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
    text-align: center;

    cursor: default;
  }

  .car .icon div{
    padding: 10px;
    border-radius: 100%;
    background-color: #dadada;
    cursor: pointer;
    transition-property: background-color;
    transition-delay: .1s;
    transition: 0.4s ease-in-out;
  }

  .car .icon div:first-child:hover{
    background-color: #00E366;
  }

  .car .icon div:last-child:hover{
    background-color: #E30000;
  }
</style>