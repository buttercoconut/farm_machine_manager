<template>
  <div id="app">
    <h1>Farm Machine Manager</h1>
    <MachineList />
  </div>
</template>

<script setup>
import MachineList from './components/MachineList.vue';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
