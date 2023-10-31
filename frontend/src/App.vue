<template>
  <div id="app">
    <HelloBanner />

    <div class="choose-area">
      <div class="mode_radio">
        <input v-model="mode" type="radio" name="mode" value="regular" id="regular" class="d-none">
        <label :class="{'selectedTable': mode === 'regular'}" for="regular">regular</label>
        <input v-model="mode" type="radio" name="mode" value="advanced" id="advanced" class="d-none">
        <label :class="{'selectedTable': mode === 'advanced'}" for="advanced">advanced</label>
      </div>
    </div>

    <TableArea v-if="mode === 'regular'"/>
    <AdvancedTableArea v-if="mode === 'advanced'"/>
    
  </div>
</template>

<script>
import HelloBanner from './components/HelloBanner.vue'
import TableArea from './components/TableArea.vue'
import AdvancedTableArea from './components/AdvancedTableArea.vue'

export default {
  name: 'App',
  components: {
    HelloBanner,
    TableArea,
    AdvancedTableArea,
  },
  data() {
    return {
      mode: "regular",
      modes:["regular", "advanced"]
    }
  }
}
</script>

<style scoped>
.choose-area{
  background-color: antiquewhite;
  display: flex;
  justify-content: center;
  padding-bottom: 30px;
}

.choose-area .mode_radio label{
  background-color: #2c3e508c;
  color: antiquewhite;
  border-radius: 50px;
  transition: all 0.3s;
  padding: 2px 10px;
  margin: 5px;
}

.choose-area .mode_radio label:hover{
  background-color: #2c3e50;
  transition: all 0.3s;
  cursor: pointer;
}

.choose-area .mode_radio .selectedTable{
  background-color: #2c3e50;
}
</style>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
