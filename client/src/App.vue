<template>
  <div id="app">
      <navigator-bar></navigator-bar>
      <router-view></router-view>
  </div>
</template>

<script>
import NavigatorBar from './components/NavigatorBar.vue'
export default {
  name: 'app',
  components: {
    NavigatorBar
  }
}
</script>

<style>

</style>
