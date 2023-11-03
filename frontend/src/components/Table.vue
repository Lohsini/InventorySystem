<template>
  <div class="table">
    <table class="table">
      <tr>
        <th v-for="(item,index) in headers" :key="index">{{item}}</th>
        <th class="edit-th" v-if="editorOn">Edit</th>
      </tr>
      <tr v-for="(item,index) in contents" :key="index">
        <td v-for="(header,key) in headers" :key="key">
          <span v-if="!editorOn">{{item[header]}}</span>
          <input type="text" v-if="editorOn" v-model="item[header]">
        </td>
        <td v-if="editorOn">
          <button class="update btn btn-primary" @click="updateItem(item)">
            Update
          </button>
          <button class="btn btn-danger" @click="dropItem(item, index)">
            Delete
          </button>
        </td>
      </tr>
      <tr>
        <td v-for="(header,key) in headers" :key="key">
          <input v-if="editorOn" type="text" :placeholder="header" v-model="newContent[header]">
        </td>
        <td v-if="editorOn">
          <button class="add-btn btn btn-success" @click="addItem(newContent)">
            Add
          </button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Table',
  props: {
    headers: {
      type: Array,
      default() {
        return []
      }
    },
    contents: {
      type: Array,
      default() {
        return []
      }
    },
    editorOn: {
      type: Boolean,
      default: false,
    },
    selectedTable: {
      type: String,
      default: "",
    }
  },
  data() {
    return {
      newContent:{},
    }
  },
  methods:{
    addItem(newContent){
      this.$emit('createData', newContent);
      this.newContent = {}
    },
    dropItem(item, index) {
      this.$emit('deleteData', item, index);
    },
    updateItem(item) {
      this.$emit('updateData', item);
    },
  },
}
</script>

<style scoped>
.table{
  width: 100%;
  margin-top: 1rem;
}
tr{
  text-align: center;
}
th{
  font-weight: 600;
  border-bottom: solid 1px black;
}
.edit-th{
  min-width:185px
}
td{
  border: none;
}
td button{
  padding: 0 6px;
  width: 80px;
}
td span{
  background-color: transparent;
  padding: 0;
  margin: 0;
}
td input{
  width: 95%;
  border: solid #555 1px;
}
.update{
  margin-right: 5px;
}
.add-btn{
  width: 165px;
}
</style>
