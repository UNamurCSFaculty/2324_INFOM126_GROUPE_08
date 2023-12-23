<template>
  <div>
    <div class="container shadow" style="width: 800px; margin-top: 5em; padding: 3em">
      <h1 class="header">QR Code Generator</h1>
      <form id="formQRCode" @submit.prevent="generateQRCode">
        <h3><center>Enter link to generate a QR code</center></h3><br>
        <div class="input-group mb-3">
          <span id="inputGroup-sizing-default" class="input-group-text">Link:</span>
          <input id="link" v-model="url" type="text" class="form-control" aria-describedby="inputGroup-sizing-default" autofocus>
        </div>
        <div class="input-group mb-3">
          <button type="submit" style="max-width: 200px; margin: auto" class="form-control btn btn-primary">Generate QR Code</button>
        </div>
      </form>
      <h4 v-if="qrcodeImage_b64"><center>QR Code:</center></h4><br>
      <div v-if="qrcodeImage_b64" class="qr-code-container" style="margin: auto; position: relative">
        <img id="qrcode" :src="'data:image/png;base64,' + qrcodeImage_b64" alt="QR Code">
      </div>
      <div v-if="qrcodeImage_b64" class="download-share-buttons">
        <button class="btn btn-primary" @click="downloadQR">Download</button>
        <button class="btn btn-primary" @click="shareQR">Share</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const url = ref('');
const qrcodeImage_b64 = ref('');

const generateQRCode = async () => {
  try {
    const response = await axios.post('/qrcode', { url: url.value }, { responseType: 'arraybuffer' });
    qrcodeImage_b64.value = btoa(String.fromCharCode(...new Uint8Array(response.data)));
    url.value = "";
  } catch (error) {
    console.error('Error generating QR code:', error);
  }
};

const downloadQR = () => {
  const link = document.createElement('a');
  link.href = 'data:image/png;base64,' + qrcodeImage_b64.value;
  link.download = 'qr_code.png';
  link.click();
};

const shareQR = () => {
  const dataUrl = 'data:image/png;base64,' + qrcodeImage_b64.value;
  if (navigator.share) {
    navigator
      .share({
        title: 'QR Code',
        text: 'Check out this QR Code',
        url: dataUrl,
      })
      .then(() => console.log('Shared successfully'))
      .catch((error) => console.log('Error sharing:', error));
  } else {
    const newWindow = window.open(dataUrl);
    if (!newWindow) {
      alert('Pop-up blocked. Please allow pop-ups for this website and try again.');
    }
  }
};
</script>

<style scoped>
body {
  background-color: #4800a3;
}

.container {
  background-color: #1a0247;
  color: white;
  border-radius: 5%;
  padding: 3em;
}

.header {
  color: white;
  text-align: center;
  margin-top: 1em;
  margin-bottom: 1em;
  font-size: 34px;
  font-weight: bold;
}

.qr-code-container {
  display: inline-block;
  position: relative;
  text-align: center;
}

.download-share-buttons {
  display: flex;
  justify-content: center;
  margin-top: 1em;
}

.download-share-buttons button {
  margin-right: 0.5em;
}

.py-2 {
  background-color: #1a0247;
}
</style>
