<template>
  <div class="advanced-table-area">

    <div class="side-nav"> 
      <h3>choose one table:</h3>
      <div class="choose-area">
        <div class="table_radio" v-for="(item,index) in tables" :key="index">
          <input v-model="selectedTable" type="radio" name="tables" :value="item" :id="item+index" >
          <label :for="item+index">{{item}}</label>
        </div>
      </div>
    </div>

    <div class="result">
      <h1>
        <span v-if="selectedTable">{{capitalizeFirstLetter(selectedTable)}}</span>
      </h1>

      <div>
        <div v-for="(item,index) in subTables" :key="index">
          <input v-model="subSelection" type="radio" name="subTables" :value="item" :id="item+index" >
          <label :for="item+index">{{item}}</label>
        </div>
      </div>

      <div class="container">
        <Table 
          :headers="headers"
          :contents="contents"
        />
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
      data:{},
      selectedTable: "sales_quantity", // default
      tables: [
        "sales_quantity",
        // "Stock Quantity",
        "Product Stock",
        "Product Out Of Stock",
        "Stock In Warehouse",
        "Running total in transaction date",
        "Average price for each product.",
        "getbuyer_ranking",
        "getprice_difference",
        "getrank1_product_in_categories",
        "getcategories_info",
        "gettransactions_num_per_month",
        "getproduct_info",
        "getmost_popular_categories",
        "getprofits",
        "getmost_popular_supplier",
        "getavg_price_in_categories",
      ],
      subSelection: "All",
      subTables: [],
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
      this.fetchTable();
    },
    subSelection() {
      this.fetchData();
    },
  },
  mounted(){
    if (this.tables) {
      this.selectedTable = this.tables[0]
    }
    this.fetchTable();
  },
  methods:{
    fetchTable(){
      if (this.selectedTable === "sales_quantity") {
        this.subTables = ["All", "Group By Products", "Group By Categories"];
        this.subSelection = this.subTables[0];
      }
      this.fetchData()
    },
    fetchData() {
      if (this.selectedTable === "sales_quantity") {
        if (this.subSelection === "Group By Products") {
          this.getSalesQuantityProducts();
        } else if (this.subSelection === "Group By Categories"){
          this.getSalesQuantityCategories();
        } else if (this.subSelection === "All"){
          this.getSalesQuantity();
        }
      } else if(this.selectedTable === "Stock In Warehouse"){
        this.getStockInWarehouse()
      } else if(this.selectedTable === "Product Stock"){
        this.getStock()
      } else if(this.selectedTable === "Product Out Of Stock"){
        this.getProductOutOfStock()
      } else if(this.selectedTable === "Running total in transaction date"){
        this.getRunningTotal();
      } else if(this.selectedTable === "Average price for each product."){
        this.getAvgPriceWindow()
      } else if(this.selectedTable === "getbuyer_ranking"){
        this.getbuyer_ranking()
      } else if(this.selectedTable === "getprice_difference"){
        this.getprice_difference()
      } else if(this.selectedTable === "getrank1_product_in_categories"){
        this.getrank1_product_in_categories()
      } else if(this.selectedTable === "getcategories_info"){
        this.getcategories_info()
      } else if(this.selectedTable === "gettransactions_num_per_month"){
        this.gettransactions_num_per_month()
      } else if(this.selectedTable === "getproduct_info"){
        this.getproduct_info()
      } else if(this.selectedTable === "getmost_popular_categories"){
        this.getmost_popular_categories()
      } else if(this.selectedTable === "getprofits"){
        this.getprofits()
      } else if(this.selectedTable === "getmost_popular_supplier"){
        this.getmost_popular_supplier()
      } else if(this.selectedTable === "getavg_price_in_categories"){
        this.getavg_price_in_categories()
      } else {
        this.data.headers = ['Not available']
      }
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    getSalesQuantity(){
      const body = {
        start_date: "2023-01-01",
        end_date: "2023-12-31",
      }
      axios.post("http://127.0.0.1:8000/advanced/sales_quantity", body)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getSalesQuantityCategories(){
      const NTILENum = 4;
      axios.get(`http://127.0.0.1:8000/advanced/sales_quantity/Categories/${NTILENum}`)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getSalesQuantityProducts(){
      const NTILENum = 3;
      axios.get(`http://127.0.0.1:8000/advanced/sales_quantity/Products/${NTILENum}`)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getRunningTotal(){
      axios.get("http://127.0.0.1:8000/advanced/running_total/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getAvgPriceWindow(){
      axios.get("http://127.0.0.1:8000/advanced/avg_price_window")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getbuyer_ranking(){
      axios.get("http://127.0.0.1:8000/advanced/buyer_ranking/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getprice_difference(){
      axios.get("http://127.0.0.1:8000/advanced/price_difference/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getrank1_product_in_categories(){
      axios.get("http://127.0.0.1:8000/advanced/rank1_product_in_categories/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getcategories_info(){
      axios.get("http://127.0.0.1:8000/advanced/categories_info/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    gettransactions_num_per_month(){
      axios.get("http://127.0.0.1:8000/advanced/transactions_num_per_month/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getproduct_info(){
      axios.get("http://127.0.0.1:8000/advanced/product_info/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getmost_popular_categories(){
      axios.get("http://127.0.0.1:8000/advanced/most_popular_categories/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getprofits(){
      axios.get("http://127.0.0.1:8000/advanced/profits/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getmost_popular_supplier(){
      axios.get("http://127.0.0.1:8000/advanced/most_popular_supplier/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getProductOutOfStock(){
      axios.get("http://127.0.0.1:8000/advanced/product_out_of_stock/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getavg_price_in_categories(){
      axios.get("http://127.0.0.1:8000/advanced/avg_price_in_categories/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getStockInWarehouse(){
      axios.get("http://127.0.0.1:8000/advanced/stock_in_warehouse/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
    },
    getStock(){
      axios.get("http://127.0.0.1:8000/advanced/stock/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
      });
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
  margin: 20px;
  font-size: 2rem;
}

.advanced-table-area{
  display: flex;
}
.side-nav{
  flex: 15%;
  background-color: rgba(252, 167, 21, 0.295);
  min-width: 230px;
  height: 100%;
  min-height: calc(100vh - 175px);
  max-height: calc(100vh - 175px);
  overflow: auto;
}
.result{
  display: flex;
  flex: 85%;
  flex-direction: column;
  justify-content: start;
}
.choose-area{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 200px;
}
.table_radio{
  margin: 0 10px;
  text-align: left;
}
.table_radio label{
  margin-left: 0px;
  margin-bottom: 10px;
}
</style>
