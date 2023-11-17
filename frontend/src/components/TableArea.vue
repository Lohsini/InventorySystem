<template>
  <div class="table-area">
    <div class="txt">
      <div class="side-nav"> 
        <div class="choose-area">
          <div class="table_radio" v-for="(item,index) in tables" :key="index">
            <input v-model="selectedTable" type="radio" name="tables" :value="item" :id="item+index" class="d-none">
            <label :for="item+index" :class="{ 'selected-label': selectedTable === item }">{{capitalizeFirstLetter(item)}}</label>
          </div>
        </div>
      </div>

      <div class="result">
        <div class="container edit-area">
          <span v-if="editorOn == true"><i class="icon fas fa-pen"></i> Edit Mode</span>
          <span v-if="editorOn == false"><i class="icon fas fa-eye"></i> Read-only Mode</span>
          <button class="change-btn mx-2 btn btn-primary" @click="turnOnEditor">
            change
          </button>
        </div>
        <h1>
          <span v-if="selectedTable">{{capitalizeFirstLetter(selectedTable)}} </span>Table
        </h1>
        
        <div class="container">
          <Table 
            :headers="headers"
            :contents="contents"
            :editorOn="editorOn"
            :selectedTable="selectedTable"
            :idList="idList"
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
      idList:{
        categoriesIdList:[],
        productsIdList:[],
        suppliersIdList:[],
        manufacturersIdList:[],
        buyersIdList:[],
        warehousesIdList:[],
        transactionsIdList:[]
      },
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
      this.getData(this.selectedTable);
    },
  },
  mounted() {
    this.init();
  },
  methods:{
    async init(){
      for (let index = 0; index < this.tables.length; index++) {
        const table = this.tables[index];
        await this.getData(table);
      }
    },
    getRowId(item) {
      if (this.selectedTable === "categories") return item.CategoriesID;
      if (this.selectedTable === "products") return item.ProductID;
      if (this.selectedTable === "suppliers") return item.SupplierID;
      if (this.selectedTable === "manufacturers") return item.ManufacturerID;
      if (this.selectedTable === "buyers") return item.BuyerID;
      if (this.selectedTable === "warehouses") return item.WarehouseID;
      if (this.selectedTable === "transactions") return item.TransactionsID;
    },
    async getData(selectedTable){
      await axios.get(`http://127.0.0.1:8000/tables/get/${selectedTable}`)
      .then((response) => {
        // Handle the response data
        if (this.selectedTable === selectedTable) {
          this.data = response.data;
        }
        if (selectedTable !== 'inventory') {
          if (selectedTable === "categories") {
            this.idList.categoriesIdList = [];
            response.data.contents.forEach(content => {
              this.idList.categoriesIdList.push(content.CategoriesID);
            });
          } else if (selectedTable === "products") {
            this.idList.productsIdList = [];
            response.data.contents.forEach(content => {
              this.idList.productsIdList.push(content.ProductID);
            });
          } else if (selectedTable === "suppliers") {
            this.idList.suppliersIdList = [];
            response.data.contents.forEach(content => {
              this.idList.suppliersIdList.push(content.SupplierID);
            });
          } else if (selectedTable === "manufacturers") {
            this.idList.manufacturersIdList = [];
            response.data.contents.forEach(content => {
              this.idList.manufacturersIdList.push(content.ManufacturerID);
            });
          } else if (selectedTable === "buyers") {
            this.idList.buyersIdList = [];
            response.data.contents.forEach(content => {
              this.idList.buyersIdList.push(content.BuyerID);
            });
          } else if (selectedTable === "warehouses") {
            this.idList.warehousesIdList = [];
            response.data.contents.forEach(content => {
              this.idList.warehousesIdList.push(content.WarehouseID);
            });
          } else if (selectedTable === "transactions") {
            this.idList.transactionsIdList = [];
            response.data.contents.forEach(content => {
              this.idList.transactionsIdList.push(content.TransactionsID);
            });
          }
        }
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
        this.getData(this.selectedTable);
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
.edit-area .icon{
  padding: 0;
  margin: 0;
  margin-right: 10px;
  align-self: center;
}
.edit-area span{
  align-self: center;
  background-color: rgb(243, 193, 29);
  width: 200px;
  border-radius: 30px;
}
.change-btn{
  background-color: #2c3e50;
}
.btn:hover{
  background-color: #2c3e50ca;
  border: #2c3e502b solid 1px;
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
  font-size: 2rem;
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
  text-align: left;
}
.table_radio label{
  padding: 20px;
  height: 50px;
  width: 200px;
}
.table_radio label:hover{
  cursor: pointer;
}
.selected-label{
  background-color: burlywood;
  font-weight: 900;
}
</style>
