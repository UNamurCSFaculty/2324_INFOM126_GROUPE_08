<script setup lang="ts">
</script>

<template>
    <form @submit.prevent="addEntree">
      <div class="mb-3">
        <label for="nom" class="form-label">Name :</label>
        <input v-model="name" type="text" class="form-control" id="nom" required>
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message :</label>
        <textarea v-model="message" class="form-control" id="message" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Send</button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        name: '',
        message: '',
      };
    },
    methods: {
      addEntree() {

        if (this.name.trim() === '' || this.message.trim() === '') {
        console.error('Please complete all fields.');
        return;
      }

      
      axios.post('/post_guest_book', {
        author: this.name,
        text: this.message,
      })
      .then(response => {
        this.$emit('add-entree', { author: this.name, text: this.message, date: response.data.date });
        this.name = '';
        this.message = '';
      })
      .catch(error => {
        console.error('Error adding message :', error);
      });

      },
    },
  };
  </script>