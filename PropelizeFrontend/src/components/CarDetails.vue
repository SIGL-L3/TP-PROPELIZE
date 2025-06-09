<script lang="ts">
import {defineComponent} from 'vue'
import  axios from 'axios'

export default defineComponent({
  name: "CarDetails",
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

  data(){
    return {
      data_updated:{
        id:Number,
        registration_number:String,
        make:String,
        model:String,
        year:Number,
        rentalprice:Number
      },
      showerror:Boolean
    }
  },

  mounted(){
    this.showerror=false
    this.data_updated = {
      id:this.id,
      registration_number:this.registration_number,
      make:this.make,
      model:this.model,
      year:this.year,
      rentalprice:this.rentalprice
    }
  },

  methods:{
    async updatecar(){
      if (this.registration_number!==this.data_updated.registration_number ||
          this.make!==this.data_updated.make ||
          this.model!==this.data_updated.model ||
          this.year!==this.data_updated.year ||
          this.make!==this.data_updated.make ||
          this.rentalprice!==this.data_updated.rentalprice
      ){
        try {
          const token = localStorage.getItem('access')
          // console.log(token)
          if(token){
            const response = await axios.patch(`http://127.0.0.1:8000/api/update/${this.id}/`,this.data_updated,
                {
                  headers:{
                    Authorization:`Bearer ${token}`,
                    'Content-Type': 'application/json'
                  }
                })
            if (response.status===200){
              this.$emit('closeupdate')
              this.$emit('updateloacle',{
                registration_number:this.data_updated.registration_number,
                make:this.data_updated.make,
                model:this.data_updated.model,
                year:this.data_updated.year,
                rentalprice:this.data_updated.rentalprice,
                id:this.data_updated.id
              })
              console.log('update succeed')
            }
          }else {
            console.log('no token')
          }
        }catch (e){
          this.showerror=true
          console.log(e)
        }
      }else {
        console.log('same')
      }
    },

    closeupdate(){
      this.$emit('closeupdate')
    }
  }
})
</script>

<template>
  <div class="bg" @click.self="closeupdate">
    <div class="content">
      <form @submit.prevent="updatecar">
        <i class="bx bx-x bx-sm " @click.self="closeupdate" style="color: gray"/>
        <p style="color: #DA0000" v-if="showerror">Registration number already taken or invalid data</p>
        <div>
          <label>registration_number</label>
          <input type="text" placeholder="registration_number"  v-model="data_updated.registration_number" autofocus>
        </div>
        <div>
          <label>make</label>
          <input type="text" placeholder="make" v-model="data_updated.make">
        </div>
        <div>
          <label>model</label>
          <input type="text" placeholder="model" v-model="data_updated.model">
        </div>
        <div>
          <label>year</label>
          <input type="number" min="0" placeholder="year" v-model="data_updated.year">
        </div>
        <div>
          <label>rental price</label>
          <input type="number" maxlength="13" placeholder="rental price" v-model="data_updated.rentalprice">
        </div>
        <button>update</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
  .content form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 15px;
  }

  .content{
    border-radius: 10px;
    background: #ffffff;
    padding: 50px 0;
    width: 550px;
  }
  .bg{
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(4px);
  }

  form input{
    height: 2rem;
    width: 100%;
    border: 1px gray solid;
    border-radius: 5px;
    padding-left: 20px;
    background: rgba(255, 255, 255, 0.17);
    color: #292929;

    font-weight: bold;
    font-size: 1rem;
  }

  form button{
    height: 2rem;
    width: 80%;
    border: none;
    border-radius: 5px;
    padding-left: 20px;
    background: rgba(255, 255, 255, 0.17);
    color: white;

    font-size: 1rem;
    background: #00E366;
    transition-property: background-color;
    transition: .2s ease-in-out;

    margin-top: 20px;
    cursor: pointer;
  }

  form button:hover{
    filter:brightness(1.2);
    scale: 1.01;
  }

  form i{
    position: relative;
    top: -40px;
    right: -250px;
    border-radius: 50%;
    transition-property: background-color;
    transition: .2s ease-in-out;
  }

  form i:hover{
    background: #e8e8e8;
  }

  form div{
    display: flex;
    flex-direction: column;
  }
  form div input{
    width: 400px;
  }

  form div label{
    color: #acacac;
  }

</style>