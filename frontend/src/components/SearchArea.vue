<template>
  <div class="search-area">
    <h1>Search</h1>
    <label for="search">search here</label>
    <input id="search" type="text">
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<style scoped>
label{
  margin: 0 10px;
}
#search{
  border-radius: 3px;
  border: 1px black solid;
}
</style>
