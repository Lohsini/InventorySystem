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
        <input v-model="selection" type="radio" name="tables" :value="item" :id="item+index" >
        <label :for="item+index">{{item}}</label>
      </div>
    </div>

    <h1>
      <span v-if="selection">{{capitalizeFirstLetter(selection)}} </span>
      Table
    </h1>

    
    <div class="container">
      <Table 
        :headers="headers"
        :contents="contents"
        :editorOn="editorOn"
        @updateItem="updateItem"
        @dropItem="dropItem"
        @addItem="addItem"
      />

      <!-- <table v-if="selection == 'categories'" class="table">
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
            <input v-if="editorOn" type="text" :placeholder="header" v-model="newRow[header]">
          </td>
          <td v-if="editorOn">
            <button class="btn btn-success" @click="addItem(newRow)">
              Add
            </button>
          </td>
        </tr>
      </table>

      <table v-if="selection == 'products'" class="table">
        <tr>
          <th v-for="(item,index) in products_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in products" :key="index">
          <td v-for="(header,key) in products_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>
      
      <table v-if="selection == 'suppliers'" class="table">
        <tr>
          <th v-for="(item,index) in suppliers_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in suppliers" :key="index">
          <td v-for="(header,key) in suppliers_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selection == 'manufacturers'" class="table">
        <tr>
          <th v-for="(item,index) in manufacturers_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in manufacturers" :key="index">
          <td v-for="(header,key) in manufacturers_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>
        
      <table v-if="selection == 'buyers'" class="table">
        <tr>
          <th v-for="(item,index) in buyers_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in buyers" :key="index">
          <td v-for="(header,key) in buyers_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selection == 'warehouses'" class="table">
        <tr>
          <th v-for="(item,index) in warehouses_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in warehouses" :key="index">
          <td v-for="(header,key) in warehouses_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selection == 'inventory'" class="table">
        <tr>
          <th v-for="(item,index) in inventory_header" :key="index">{{item}}</th>
        </tr>
        <tr v-for="(item,index) in inventory" :key="index">
          <td v-for="(header,key) in inventory_header" :key="key">
            {{item[header]}}
          </td>
        </tr>
      </table>

      <table v-if="selection == 'transactions'" class="table">
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

export default {
  name: 'TableArea',
  components:{
    Table,
  },
  data() {
    return {
      editorOn: false,
      selection:"categories",
      tables:["categories","products","suppliers","manufacturers","buyers","warehouses","inventory","transactions"],

      categories_header:["CategoriesID", "CategoriesName", "CategoriesDescription"],
      products_header:["ProductID", "ProductName", "Price", "Cost", "CategoriesID", "SupplierID", "ManufacturerID"],
      suppliers_header:["SupplierID", "SupplierName", "ContactDetail_Phone", "ContactDetail_Email"],
      manufacturers_header:["ManufacturerID", "ManufacturerName", "ContactDetail_Phone", "ContactDetail_Email"],
      buyers_header:["BuyerID", "name_Firstname", "name_Lastname", "ContactDetail_Phone", "ContactDetail_Email"],
      warehouses_header:["WarehouseID", "State", "City"],
      inventory_header:["ProductID", "WarehouseID", "Quantity"],
      transactions_header:["TransactionsID", "BuyerID", "ProductID", "Quantity", "TransactionsDate"],

      categories:[
        {"CategoriesID": 1, "CategoriesName": "Category 1", "CategoriesDescription": "Description 1"},
        {"CategoriesID": 2, "CategoriesName": "Category 2", "CategoriesDescription": "Description 2"},
      ],
      products:[
        {"ProductID": 1, "ProductName": "Product 1", "Price": 10.99, "Cost": 5.99, "CategoriesID": 1, "SupplierID": 1, "ManufacturerID": 1},
        {"ProductID": 2, "ProductName": "Product 2", "Price": 15.99, "Cost": 8.99, "CategoriesID": 2, "SupplierID": 2, "ManufacturerID": 2},
      ],
      suppliers:[
        {"SupplierID": 1, "SupplierName": "Supplier 1", "ContactDetail_Phone": "123-456-7890", "ContactDetail_Email": "supplier1@example.com"},
        {"SupplierID": 2, "SupplierName": "Supplier 2", "ContactDetail_Phone": "987-654-3210", "ContactDetail_Email": "supplier2@example.com"},
      ],
      manufacturers:[
        {"ManufacturerID": 1, "ManufacturerName": "Manufacturer 1", "ContactDetail_Phone": "111-222-3333", "ContactDetail_Email": "manufacturer1@example.com"},
        {"ManufacturerID": 2, "ManufacturerName": "Manufacturer 2", "ContactDetail_Phone": "444-555-6666", "ContactDetail_Email": "manufacturer2@example.com"},
      ],
      buyers:[
        {"BuyerID": 1, "name_Firstname": "John", "name_Lastname": "Doe", "ContactDetail_Phone": "555-123-4567", "ContactDetail_Email": "john.doe@example.com"},
        {"BuyerID": 2, "name_Firstname": "Jane", "name_Lastname": "Smith", "ContactDetail_Phone": "777-987-6543", "ContactDetail_Email": "jane.smith@example.com"},
      ],
      warehouses:[
        {"WarehouseID": 1, "State": "California", "City": "Los Angeles"},
        {"WarehouseID": 2, "State": "New York", "City": "New York City"},
      ],
      inventory:[
        {"ProductID": 1, "WarehouseID": 1, "Quantity": 100},
        {"ProductID": 2, "WarehouseID": 1, "Quantity": 50},
      ],
      transactions:[
        {"TransactionsID": 1, "BuyerID": 1, "ProductID": 1, "Quantity": 10, "TransactionsDate": "2023-10-30"},
        {"TransactionsID": 2, "BuyerID": 2, "ProductID": 2, "Quantity": 5, "TransactionsDate": "2023-10-31"},
      ],
    };
  },
  computed: {
    headers() {
      return this[`${this.selection}_header`];
    },
    contents() {
      return this[this.selection];
    }
  },
  methods:{
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
      }
    },
    updateItem(item,index) {
      console.log("updateItem", item, index);
    },
    dropItem(index) {
      this[this.selection].splice(index, 1);
    },
    addItem(newRow){
      this[this.selection].push(newRow);
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
