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

      <!-- <table v-if="selectedTable == 'categories'" class="table">
        <tr>
          <th v-for="(item,index) in categories_header" :key="index">{{item}}</th>
          <th v-if="editorOn">Edit</th>
        </tr>
        <tr v-for="(item,index) in categories" :key="index">
          <td v-for="(header,key) in categories_header" :key="key">
            <span v-if="!editorOn">{{item[header]}}</span>
            <input type="text" v-if="editorOn" v-model="item[header]">
          </td>
          <td v-if="editorOn">
            <button class="update btn btn-primary" @click="updateItem(item,index)">
              update
            </button>
            <button class="btn btn-danger" @click="dropItem(item,index)">
              Drop
            </button>
          </td>
        </tr>
        <tr>
          <td v-for="(header,key) in categories_header" :key="key">
            <input v-if="editorOn" type="text" :placeholder="header" v-model="newContent[header]">
          </td>
          <td v-if="editorOn">
            <button class="btn btn-success" @click="addItem(newContent)">
              Add
            </button>
          </td>
        </tr>
      </table>

      <table v-if="selectedTable == 'products'" class="table">
        <tr>
          <th v-for="(item,index) in products_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in products" :key="index">
          <td v-for="(header,key) in products_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>
      
      <table v-if="selectedTable == 'suppliers'" class="table">
        <tr>
          <th v-for="(item,index) in suppliers_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in suppliers" :key="index">
          <td v-for="(header,key) in suppliers_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selectedTable == 'manufacturers'" class="table">
        <tr>
          <th v-for="(item,index) in manufacturers_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in manufacturers" :key="index">
          <td v-for="(header,key) in manufacturers_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>
        
      <table v-if="selectedTable == 'buyers'" class="table">
        <tr>
          <th v-for="(item,index) in buyers_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in buyers" :key="index">
          <td v-for="(header,key) in buyers_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selectedTable == 'warehouses'" class="table">
        <tr>
          <th v-for="(item,index) in warehouses_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in warehouses" :key="index">
          <td v-for="(header,key) in warehouses_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selectedTable == 'inventory'" class="table">
        <tr>
          <th v-for="(item,index) in inventory_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in inventory" :key="index">
          <td v-for="(header,key) in inventory_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selectedTable == 'transactions'" class="table">
        <tr>
          <th v-for="(item,index) in transactions_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in transactions" :key="index">
          <td v-for="(header,key) in transactions_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table> -->
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
    deleteData(index){
      this.data.contents.splice(index, 1);
      axios.put(`http://127.0.0.1:8000/tables/delete/${this.selectedTable}?row_index=${index}`)
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
    updateData(newContent, index){
      const body = newContent
      axios.post(`http://127.0.0.1:8000/tables/update/${this.selectedTable}?row_index=${index}`, body)
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
