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
    
      <tr v-if="selectedTable !=='inventory'">
        <td v-for="(header,key) in headers" :key="key">
          <input 
            class="disabled_input"
            v-if="editorOn && key == 0" 
            type="text" 
            :placeholder="header" 
            :value="getTableID(headers[0])"
            disabled 
          >
          <input 
            v-if="editorOn && key > 0 && header !== 'CategoriesID' && header !== 'ProductID' && header !== 'SupplierID' && header !== 'ManufacturerID' && header !== 'BuyerID'" 
            type="text"
            :placeholder="header" 
            v-model="newContent[header]"
          >
          <select 
            v-if="editorOn && key > 0 && header === 'CategoriesID'"
            id="dropdown"
            name="dropdown"
            v-model="newContent.CategoriesID"
          >
            <option selected disabled value="">CategoriesID</option>
            <option v-for="(id, key) in idList.categoriesIdList" :key="key" :value="id">{{id}}</option>
          </select>
          <select 
            v-if="editorOn && key > 0 && header === 'ProductID'"
            id="dropdownProductID"
            name="dropdown"
            v-model="newContent.ProductID"
          >
            <option selected disabled value="">ProductID</option>
            <option v-for="(id, key) in idList.productsIdList" :key="key" :value="id">{{id}}</option>
          </select>
          <select 
            v-if="editorOn && key > 0 && header === 'SupplierID'"
            id="dropdownSupplierID"
            name="dropdown"
            v-model="newContent.SupplierID"
          >
            <option selected disabled value="">SupplierID</option>
            <option v-for="(id, key) in idList.suppliersIdList" :key="key" :value="id">{{id}}</option>
          </select>
          <select 
            v-if="editorOn && key > 0 && header === 'ManufacturerID'"
            id="dropdownManufacturerID"
            name="dropdown"
            v-model="newContent.ManufacturerID"
          >
            <option selected disabled value="">ManufacturerID</option>
            <option v-for="(id, key) in idList.manufacturersIdList" :key="key" :value="id">{{id}}</option>
          </select>
          <select 
            v-if="editorOn && key > 0 && header === 'BuyerID'"
            id="dropdownBuyerID"
            name="dropdown"
            v-model="newContent.BuyerID"
          >
            <option selected disabled value="">BuyerID</option>
            <option v-for="(id, key) in idList.buyersIdList" :key="key" :value="id">{{id}}</option>
          </select>
        </td>
        <td v-if="editorOn">
          <button class="add-btn btn btn-success" @click="addItem(newContent)">
            Add
          </button>
        </td>
      </tr>

        
      <tr v-if="selectedTable ==='inventory'">
        <td v-for="(header,key) in headers" :key="key">
          <select 
            v-if="editorOn && header === 'ProductID'"
            id="dropdownProductID2"
            name="dropdown"
            v-model="newContent.ProductID"
          >
            <option selected disabled value="">ProductID</option>
            <option v-for="(id, key) in idList.productsIdList" :key="key" :value="id">{{id}}</option>
          </select>
          <select 
            v-if="editorOn && header === 'WarehouseID'"
            id="dropdownWarehouseID"
            name="dropdown"
            v-model="newContent.WarehouseID"
          >
            <option selected disabled value="">WarehouseID</option>
            <option v-for="(id, key) in idList.warehousesIdList" :key="key" :value="id">{{id}}</option>
          </select>
          <input 
            v-if="editorOn && key === 2" 
            type="text" 
            :placeholder="header" 
            v-model="newContent[header]"
          >
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
    },
    idList: {
      type: Object,
      default() {
        return {
          categoriesIdList: [],
          productsIdList: [],
          suppliersIdList: [],
          manufacturersIdList: [],
          buyersIdList: [],
          warehousesIdList: [],
          transactionsIdList: []
        };
      }
    }
  },
  data() {
    return {
      newContent:{
      },
      nextID: "",
    }
  },
  watch: {
  },
  mounted(){
  },
  methods:{
    addItem(newContent){
      if (this.selectedTable !=='inventory') {
        newContent[this.headers[0]] = this.nextID;
      }
      console.log(this.newContent);
      this.$emit('createData', newContent);
      this.newContent = {}
    },
    dropItem(item, index) {
      this.$emit('deleteData', item, index);
    },
    updateItem(item) {
      this.$emit('updateData', item);
    },
    getTableID(idName) {
      let result = "";
      const id = this.contents[this.contents.length - 1][idName];
      const letterPart = id[0];
      const numberPart = parseInt(id.slice(1), 10);
      const newNumberPart = numberPart + 1;
      result = letterPart + newNumberPart;
      this.nextID = result;
      return result;
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
tr .disabled_input:hover{
  cursor: not-allowed;
}
select{
  width: 95%;
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
