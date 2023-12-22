<script setup lang="ts">
import QRCodeGenerator from './components/QRCodeGenerator.vue';
import { ref } from 'vue';
import GuestBookForm from './components/GuestBookForm.vue';
import GuestBookList from './components/GuestBookList.vue';
import FooterComp from './components/FooterComp.vue';

interface GuestBookEntry {
  author: string;
  text: string;
  date: string; 
}

const entries = ref<GuestBookEntry[]>([]);
</script>

<template>
  <div class="principal-container">
    <QRCodeGenerator />
    <div class="guest-book-container">
      <GuestBookList :entries="entries"></GuestBookList>
      <GuestBookForm @add-entry="(newEntry: GuestBookEntry) => entries.push(newEntry)"></GuestBookForm>
    </div>
    <FooterComp />
  </div>
</template>

<style scoped>
.principal-container {
  background-color: #ff0f5f;
  color: white;
  border-radius: 5px;
  padding: 15px;
  margin-top: 10px;
}

.guest-book-container {
  background-color: #1a0247;
  color: white;
  border-radius: 15px;
  padding: 15px;
  margin-top: 30px;

}
</style>
