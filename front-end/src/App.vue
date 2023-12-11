<script setup lang="ts">
import { ref, defineProps } from 'vue';
//import HelloWorld from './components/HelloWorld.vue';
import GuestBookForm from './components/GuestBookForm.vue';
import GuestBookList from './components/GuestBookList.vue';

const props = defineProps(['addEntree']);
const entries = ref([]);
</script>

<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/assets/guest-book-svgrepo-com.svg" class="logo" alt="Guest Book Logo" />
    </a>
  </div>
   <!--<HelloWorld msg="Vite + Vue" /> -->
  <div>
    <h1>Guest Book</h1>
    <div class="guest-book-list-container">
      <GuestBookList :entries="entries"></GuestBookList>
    </div>

    <div class="guest-book-form-container">
      <GuestBookForm @add-entree="props.addEntree"></GuestBookForm>
    </div>
  </div>
</template>

<style scoped>
.logo {
  height: 8em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.guest-book-list-container {
  border: 3px solid #ddd;
  padding: 10px;
  margin-bottom: 20px;
}

.guest-book-form-container {
  border: 3px solid #ddd;
  padding: 10px;
}
</style>
