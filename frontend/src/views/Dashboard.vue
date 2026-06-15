
// src/views/Dashboard.vue
<template>
  <div class="dashboard">
    <h1>Farm Machine Manager Dashboard</h1>
    <nav>
      <router-link to="/machines">Machines</router-link> |
      <router-link to="/rentals">Rentals</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
// Dashboard view logic if needed
</script>

<style scoped>
.dashboard {
  padding: 20px;
}
nav {
  margin-bottom: 20px;
}
nav a {
  margin-right: 10px;
}
</style>
