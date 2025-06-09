<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Deletepopup",

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

  methods:{
    deletecar(){
      this.$emit('closeDeltePopoUp')
      this.$emit('deletecar',this.id)
    },

    closeDeltePopoUp(){
      this.$emit('closeDeltePopoUp')
    }
  }

})
</script>

<template>
  <div class="bg" @click.self="closeDeltePopoUp">
    <form @submit.prevent="deletecar">
      <p style="opacity: 50%">voulez vous vraiment suprimer ce vehicule ?</p>
      <div class="content">
        <p><span>Registration number</span> : {{registration_number}}</p>
        <p><span>Make</span> : {{make}}</p>
        <p><span>Model</span> : {{model}}</p>
        <p><span>Year</span> : {{year}}</p>
        <p><span>Rental price</span> : {{rentalprice}} $</p>
      </div>
      <div class="btn">
        <button type="button" @click="closeDeltePopoUp">x</button>
        <button type="submit">oui</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
  form{
    font-size: 14px;
  }
  div{
    color: #181818;
  }

  form{
    background-color: white;
    padding: 32px;
    border-radius: 8px;

    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
  }
  .content{
    background-color: #f6f6f6;
    border-radius: 8px;
    padding: 16px;
  }

  .content p{
    font-weight: bolder;
  }

  .bg{
    background-color: rgba(0, 0, 0, 0.25);
    width: 100vw;
    height: 100vh;
    position: absolute;
    top: 0;
    left: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    backdrop-filter: blur(4px);
  }

  form button, .btn div{
    border: none;
    background-color: #ff1b1b;
    border-radius: 4px;
    padding: 8px;
    width: 70%;
    color: white;
    font-weight: bolder;
  }

  .btn{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 80%;
    height: 30px;

    gap: 16px;
  }

  .btn button{
    width: 80%;
    height: 30px;
  }

  .btn button:first-child{
    width: 20%;
    display: flex;
    align-items: center;
    justify-content: center;

    background-color: #dadada;
    height: 30px;
  }

  .btn button{
    transition-property: background-color;
    transition: .2s ease-in-out;
  }


  .btn button:hover{
    filter: brightness(1.1);
    scale: 1.02;
  }

  span{
    color: gray;
  }

  form{
    transform: scale(1.3);
  }
</style>