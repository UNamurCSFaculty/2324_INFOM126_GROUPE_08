<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const url = ref('');
const qrcodeUrl = ref('');

const generateQRCode = async () => {
  try {
    console.log('Sending URL:', url.value);
    
    const response = await axios.post('/qrcode', { url: url.value });
    
    console.log(response);

    qrcodeUrl.value = response.data;

  } catch (error) {
    console.error('Error generating QR code:', error);
  }
};
</script>


<template>
  <div class="container mt-5">
    <h1 class="mb-4">QR Code Generator</h1>
    <form id="qrCodeForm" @submit.prevent="generateQRCode">
      <div class="mb-3">
        <label for="url" class="form-label">URL:</label>
        <input v-model="url" type="text" class="form-control" id="url" required>
      </div>
      <button type="submit" class="btn btn-primary">Generate QR Code</button>
    </form>
    <div id="qrcode" class="mt-4">
      <img :src="qrcodeUrl" alt="Generated QR Code" v-if="qrcodeUrl">
    </div>
  </div>
</template>

<style scoped>
</style>
