<script setup lang="ts">
import QRCodeGenerator from './components/QRCodeGenerator.vue';
import {defineProps, ref} from 'vue';
import GuestBookForm from './components/GuestBookForm.vue';
import GuestBookList from './components/GuestBookList.vue';
import FooterComp from './components/FooterComp.vue';

const props = defineProps<{addEntree: any}>();
const entries = ref([]);
</script>

<template>
  <div class="principal-container">
    <QRCodeGenerator />
    <div class="guest-book-container">
      <GuestBookList :entries="entries"></GuestBookList>
      <GuestBookForm @add-entree="props.addEntree"></GuestBookForm>
    </div>
    <FooterComp />
  </div>
</template>

<style scoped>
.principal-container {
  background-color: #2b0f5f;
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
