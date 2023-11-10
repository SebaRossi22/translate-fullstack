<template>
    <div>
        <div class="input-group">
            <textarea v-model="text" class="form-control" aria-label="With textarea"></textarea>
            <button @click="handleAddSubmit" type="button" class="btn btn-outline-primary">Translate</button>
        </div>
        <div v-if="testo" class="alert alert-danger" role="alert">
            Inserisci del testo da tradurre!
        </div>
        <p v-else>Translation: {{ translation }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        text: '',
        translation: '',
        testo: false,
      };
    },
    methods: {
      handleAddSubmit() {
        if(this.text != ""){
            this.testo = false;
            const payload = {
            text: this.text.toString()
            };
            this.addBook(payload);
            this.text = "";
        }else{
            this.testo = true;
        }
      },
      addBook(payload) {
      const path = 'http://localhost:5001/translate';
      axios.post(path, payload)
        .then((res) => {
          this.translation = res.data.translation;
        })  
        .catch((error) => {
          console.error(error);
        });
      },
    },
  };
  </script>