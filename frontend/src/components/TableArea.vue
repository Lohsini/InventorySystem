<template>
  <div class="table-area">

    <div class="container edit-area">
      <span v-if="editorOn == true">Edit Mode</span>
      <span v-if="editorOn == false">Read Mode</span>
      <button class="mx-2 btn btn-primary" @click="turnOnEditor">
        change
      </button>
    </div>

    <h3>You can choose one table here:</h3>
    <div class="choose-area">
      <div class="table_radio" v-for="(item,index) in tables" :key="index">
        <input v-model="selectedTable" type="radio" name="tables" :value="item" :id="item+index" >
        <label :for="item+index">{{item}}</label>
      </div>
    </div>

    <h1>
      <span v-if="selectedTable">{{capitalizeFirstLetter(selectedTable)}} </span>
      Table
    </h1>

    
    <div class="container">
      <Table 
        :headers="headers"
        :contents="contents"
        :editorOn="editorOn"
        @createData="createData"
        @deleteData="deleteData"
        @updateData="updateData"
      />
    </div>

  </div>
</template>

<script>
import Table from './Table.vue'
import axios from 'axios';

export default {
  name: 'TableArea',
  components:{
    Table,
  },
  data() {
    return {
      data: {},
      editorOn: false,
      selectedTable:"categories", // default is "categories"
      tables:[
        "categories",
        "products",
        "suppliers",
        "manufacturers",
        "buyers",
        "warehouses",
        "inventory",
        "transactions"
      ],
    };
  },
  computed: {
    headers() {
      return this.data.headers;
    },
    contents() {
      return this.data.contents;
    }
  },
  watch: {
    selectedTable() {
      this.getData();
    },
  },
  mounted() {
    this.getData();
  },
  methods:{
    getRowId(item) {
      if (item.CategoriesID) return item.CategoriesID;
      if (item.ProductID) return item.ProductID;
      if (item.SupplierID) return item.SupplierID;
      if (item.ManufacturerID) return item.ManufacturerID;
      if (item.BuyerID) return item.BuyerID;
      if (item.WarehouseID) return item.WarehouseID;
      if (item.TransactionsID) return item.TransactionsID;
    },
    getData(){
      axios.get(`http://127.0.0.1:8000/tables/get/${this.selectedTable}`)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    createData(newContent){
      this.data.contents.push(newContent);
      const body = newContent
      axios.post(`http://127.0.0.1:8000/tables/create/${this.selectedTable}`, body)
      .then((response) => {
        // Handle the response data
        const data = response.data;
        console.log(data);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    deleteData(item, index){
      this.data.contents.splice(index, 1);
      if (this.selectedTable === 'inventory') {
        axios.put(`http://127.0.0.1:8000//tables/delete/inventory/${item.ProductID}/${item.WarehouseID}`)
        .then((response) => {
          // Handle the response data
          const data = response.data;
          console.log(data);
        })
        .catch((error) => {
          // Handle any errors
          console.error('Error:', error);
        });
      } else {
        axios.put(`http://127.0.0.1:8000/tables/delete/${this.selectedTable}/${this.getRowId(item)}`)
        .then((response) => {
          // Handle the response data
          const data = response.data;
          console.log(data);
        })
        .catch((error) => {
          // Handle any errors
          console.error('Error:', error);
        });
      }
    },
    updateData(newContent){
      const body = newContent
      axios.post(`http://127.0.0.1:8000/tables/update/${this.selectedTable}`, body)
      .then((response) => {
        // Handle the response data
        const data = response.data;
        console.log(data);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    turnOnEditor(){
      this.editorOn = !this.editorOn
      if (this.editorOn == true) {
        console.log("start to edit"); 
      }
      if (this.editorOn == false) {
        console.log("end and save"); 
        this.getData();
      }
    },
  },
}
</script>

<style scoped>
.edit-area{
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}
.edit-area span{
  border: solid 1px black;
  border-radius: 2px;
  color: black;
  width: 100px;
}
button{
  padding: 0 6px;
}
h3{
  margin-top: 30px;
  font-size: 1.2rem;
}
h1{
  margin: 0;
}
.choose-area{
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
  margin-top: 20px;
}
.table_radio{
  margin: 0 10px;
}
.table_radio label{
  margin-left: 5px;
}
</style>
