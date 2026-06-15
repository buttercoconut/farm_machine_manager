
// src/views/MachineManagement.vue
<template>
  <div class="machine-management">
    <h2>Machine Management</h2>
    <MachineList />
  </div>
</template>

<script setup>
import MachineList from '../components/MachineList.vue';
</script>

<style scoped>
.machine-management {
  padding: 20px;
}
</style>
