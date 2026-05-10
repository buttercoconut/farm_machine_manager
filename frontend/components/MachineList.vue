<template>
  <div>
    <h2>Machine List</h2>
    <ul>
      <li v-for="machine in machines" :key="machine.id">
        {{ machine.model }} ({{ machine.manufacturer }}) - {{ machine.serial_number }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const machines = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get('/api/machines');
    machines.value = response.data;
  } catch (err) {
    console.error('Failed to fetch machines', err);
  }
});
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 0.5rem;
}
</style>
