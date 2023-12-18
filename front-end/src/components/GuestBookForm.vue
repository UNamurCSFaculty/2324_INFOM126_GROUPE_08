<template>
  <form id="formGuestBook" @submit.prevent="addEntree">
    <div class="mb-3">
      <label for="nom" class="form-label">Name</label>
      <input id="nom" v-model="author" type="text" class="form-control" required>
    </div>
    <div class="mb-3">
      <label for="message" class="form-label">Message</label>
      <textarea id="message" v-model="message" class="form-control" required></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Send</button>
  </form>
  <p class="response-message">{{ requestResp }}</p>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const emit = defineEmits<{
  (e: 'add-entry', entry: any): any
}>();

const author = ref('');
const message = ref('');
const requestResp = ref('');

const addEntree = async () => {
  try {
    // fetch back api
    const response = await axios.post('/guest-book', {
      author: author.value,
      text: message.value,
    });

    // reset inputs
    author.value = '';
    message.value = '';

    // set the reponse from the back as the new requestResp
    requestResp.value = response.data.message;

    // emit "add-entry" event with the given new entry
    emit('add-entry', response.data.entry);
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
