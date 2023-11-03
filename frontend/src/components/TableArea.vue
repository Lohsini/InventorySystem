<template>
  <div class="table-area">


    <div class="txt">
      <div class="side-nav"> 
        <h3>choose one table here:</h3>
        <div class="choose-area">
          <div class="table_radio" v-for="(item,index) in tables" :key="index">
            <input v-model="selectedTable" type="radio" name="tables" :value="item" :id="item+index" >
            <label :for="item+index">{{item}}</label>
          </div>
        </div>
      </div>

      <div class="result">
        <div class="container edit-area">
          <span v-if="editorOn == true">Edit Mode</span>
          <span v-if="editorOn == false">Read Mode</span>
          <button class="mx-2 btn btn-primary" @click="turnOnEditor">
            change
          </button>
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
            :selectedTable="selectedTable"
            @createData="createData"
            @deleteData="deleteData"
            @updateData="updateData"
          />
        </div>
      </div>
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
      if (this.selectedTable === "categories") return item.CategoriesID;
      if (this.selectedTable === "products") return item.ProductID;
      if (this.selectedTable === "suppliers") return item.SupplierID;
      if (this.selectedTable === "manufacturers") return item.ManufacturerID;
      if (this.selectedTable === "buyers") return item.BuyerID;
      if (this.selectedTable === "warehouses") return item.WarehouseID;
      if (this.selectedTable === "transactions") return item.TransactionsID;
    },
    getData(){
      axios.get(`http://127.0.0.1:8000/tables/get/${this.selectedTable}`)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error("Error: Fail", error);
        window.alert("Error: Fail");
      });
    },
    createData(newContent){
      const body = newContent;
      axios.post(`http://127.0.0.1:8000/tables/create/${this.selectedTable}`, body)
      .then((response) => {
        // Handle the response data
        const data = response.data;
        console.log(data);
        this.data.contents.push(newContent);
        window.alert("Success");
      })
      .catch((error) => {
        // Handle any errors
        console.error("Error: Fail", error);
        window.alert("Error: Fail");
      });
    },
    deleteData(item, index){
      if (this.selectedTable === 'inventory') {
        axios.put(`http://127.0.0.1:8000//tables/delete/inventory/${item.ProductID}/${item.WarehouseID}`)
        .then((response) => {
          // Handle the response data
          const data = response.data;
          console.log(data);
          window.alert("Success");
          this.data.contents.splice(index, 1);
        })
        .catch((error) => {
          // Handle any errors
          console.error("Error: Fail", error);
          window.alert("Error: Fail");
        });
      } else {
        axios.put(`http://127.0.0.1:8000/tables/delete/${this.selectedTable}/${this.getRowId(item)}`)
        .then((response) => {
          // Handle the response data
          const data = response.data;
          console.log(data);
          window.alert("Success");
          this.data.contents.splice(index, 1);
        })
        .catch((error) => {
          // Handle any errors
          console.error("Error: Fail", error);
          window.alert("Error: Fail");
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
        window.alert("Success");
      })
      .catch((error) => {
        // Handle any errors
        console.error("Error: Fail", error);
        window.alert("Error: Fail");
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
.txt{
  display: flex;
}
.side-nav{
  flex: 15%;
  background-color: rgba(252, 167, 21, 0.295);
  min-width: 230px;
  min-height: calc(100vh - 175px);
  max-height: calc(100vh - 175px);
  overflow: auto;
}
.result{
  display: flex;
  flex: 85%;
  flex-direction: column;
  justify-content: start;
  overflow: auto;
  max-height: calc(100vh - 178px);
}
.choose-area{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin-bottom: 50px;
  margin-top: 20px;
  width: 200px;
}
.table_radio{
  margin: 0 20px;
  text-align: left;
}
.table_radio label{
  margin-left: 10px;
  margin-bottom: 10px;
}
</style>
