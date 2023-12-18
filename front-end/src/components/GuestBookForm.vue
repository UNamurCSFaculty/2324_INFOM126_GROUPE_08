<template>
  <form id="formGuestBook" @submit.prevent="addEntree">
    <div class="mb-3">
      <label for="nom" class="form-label">Name</label>
      <input id="nom" v-model="name" type="text" class="form-control" required>
    </div>
    <div class="mb-3">
      <label for="message" class="form-label">Message</label>
      <textarea id="message" v-model="message" class="form-control" required></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Send</button>
  </form>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const name = ref('');
const message = ref('');

const addEntree = async () => {
  try {
    const response = await axios.post('/guest-book', {
      author: name.value,
      text: message.value,
    });

    console.log(response.data);
    name.value = '';
    message.value = '';
    location.reload();
  } catch (error) {
    console.error('Error adding entry:', error);
  }
};
</script>

<style scoped>
.guest-book-form-container label {
  color: white;
}
.guest-book-form-container input,
.guest-book-form-container textarea {
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 5px;
  width: 100%;
}
.guest-book-form-container button {
  background-color: #0d6efd;
  color: white;
  border: none;
  max-width: 250px;
  margin: auto;
  border-radius: 3px;
  cursor: pointer;
}
.guest-book-form-container button:hover {
  background-color: #0a58ca;
}

.header {
  color: white;
  text-align: center;
  margin-top: 1em;
  margin-bottom: 1em;
  font-size: 34px;
  font-weight: bold;
}
</style>
