<template>
  <div>
    <h2>Messages Guest Book</h2>
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
</style>
