<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const url = ref('');
const qrcodeImage_b64 = ref('');

const generateQRCode = async () => {
  try {
    const response = await axios.post('/qrcode', { url: url.value}, { responseType: "arraybuffer" });
    qrcodeImage_b64.value = btoa(String.fromCharCode(...new Uint8Array(response.data)));
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
        <input v-model="url" type="text" class="form-control" id="url" placeholder="https://example.com" required>
      </div>
      <button type="submit" class="btn btn-primary">Generate QR Code</button>
    </form>
    <div id="qrcode" class="mt-4">
      <img :src="'data:image/png;base64,' + qrcodeImage_b64" alt="Generated QR Code" v-if="qrcodeImage_b64">
    </div>
  </div>
</template>

<style scoped>
</style>
