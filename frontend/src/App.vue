<template>
  <div id="app">
    <HelloBanner />

    <div class="choose-area">
      <div class="mode_radio">
        <input v-model="mode" type="radio" name="mode" value="Basic" id="Basic" class="d-none">
        <label :class="{'selectedTable': mode === 'Basic'}" for="Basic">Basic</label>
        <input v-model="mode" type="radio" name="mode" value="Advanced" id="Advanced" class="d-none">
        <label :class="{'selectedTable': mode === 'Advanced'}" for="Advanced">Advanced</label>
      </div>
    </div>

    <BasicTableArea v-if="mode === 'Basic'"/>
    <AdvancedTableArea v-if="mode === 'Advanced'"/>
    
  </div>
</template>

<script>
import HelloBanner from './components/HelloBanner.vue'
import BasicTableArea from './components/BasicTableArea.vue'
import AdvancedTableArea from './components/AdvancedTableArea.vue'

export default {
  name: 'App',
  components: {
    HelloBanner,
    BasicTableArea,
    AdvancedTableArea,
  },
  data() {
    return {
      mode: "Basic",
      modes:["Basic", "Advanced"]
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
  box-shadow: 0 8px 10px #2c3e5019;
  /* padding-left: 230px; */
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
  font-family: Quicksand, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
