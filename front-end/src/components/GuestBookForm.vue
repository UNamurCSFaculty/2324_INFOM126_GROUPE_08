
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