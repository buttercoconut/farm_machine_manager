
// src/components/MachineList.vue
<template>
  <div class="machine-list">
    <h3>Machine List</h3>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Model</th>
          <th>Manufacturer</th>
          <th>Purchase Date</th>
          <th>Serial Number</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="machine in machines" :key="machine.id">
          <td>{{ machine.id }}</td>
          <td>{{ machine.model }}</td>
          <td>{{ machine.manufacturer }}</td>
          <td>{{ machine.purchase_date }}</td>
          <td>{{ machine.serial_number }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const machines = ref([]);

const fetchMachines = async () => {
  try {
    const response = await axios.get('/api/machines');
    machines.value = response.data;
  } catch (error) {
    console.error('Error fetching machines:', error);
  }
};

onMounted(() => {
  fetchMachines();
});
</script>

<style scoped>
.machine-list {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}
</style>
