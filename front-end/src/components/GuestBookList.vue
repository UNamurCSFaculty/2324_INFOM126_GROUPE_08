<template>
  <div>
    <h1 class="header">Guest Book</h1>
    <div>
      <img src="/assets/guest-book-svgrepo-com.svg" class="logo" alt="Guest Book Logo" />
  </div>
    
    <div class="guest-book-list-container">
    <div class="table-container">
      <table name="table-guest-book" class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Message</th>
            <th scope="col">Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entree, index) in entries" :key="index">
            <td>{{ entree.author }}</td>
            <td class="justified-text">{{ entree.text }}</td>
            <td>{{ entree.date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  interface GuestBookEntry {
    author: string;
    text: string;
    date: string; 
  }

  const entries = ref<GuestBookEntry[]>([]);

  onMounted(async () => {
    try {
      const response = await axios.get('/guest-book');
      entries.value = response.data.entries;
      console.log('Data from server:', entries.value);
    } catch (error) {
      console.error('Error fetching entries:', error);
    }
  });
</script>

<style scoped>
  .table-container {
    margin-top: 20px;
  }

  .justified-text {
    text-align: justify;
  }



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

</style>
