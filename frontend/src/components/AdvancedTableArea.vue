<template>
  <div class="advanced-table-area">
    <div class="txt">
      <div class="side-nav"> 
        <div class="choose-area">
          <div class="table_radio" v-for="(item,index) in sections" :key="index">
            <input v-model="selectedSections" type="radio" name="sections" :value="item" :id="item+index" class="d-none">
            <label :for="item+index" :class="{ 'selected-label': selectedSections === item }">{{item}}</label>
          </div>
        </div>
      </div>

      <div class="result">
        <h1>
          <span v-if="selectedSections">{{capitalizeFirstLetter(selectedSections)}}</span>
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
      selectedSections: "Quantity Sold", // default
      sections: [
        "Quantity Sold",
        "Popular Ranking",
        "Inventory",
        "Revenue",
        "Infomation",
        "Others"
      ],
      subSelection: "",
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
    selectedSections() {
      this.fetchTable();
    },
    subSelection() {
      this.fetchData();
    },
  },
  mounted(){
    if (this.sections) {
      this.selectedSections = this.sections[0]
    }
    this.fetchTable();
  },
  methods:{
    fetchTable(){
      if (this.selectedSections === "Quantity Sold") {
        this.subTables = [
          "Transactions Information",
          "Group By Products",
          "Group By Categories"
        ];
      } else if (this.selectedSections === "Popular Ranking") {
        this.subTables = [
          "getmost_popular_categories",
          "getmost_popular_supplier",
          "getrank1_product_in_categories",
          "getbuyer_ranking"
        ]
      } else if (this.selectedSections === "Inventory") {
        this.subTables = [
          "Stock In Warehouse", 
          "Product Stock", 
          "Product Out Of Stock"
        ];
      } else if (this.selectedSections === "Revenue") {
        this.subTables = [
          "Cumulative Revenue Group By Date",
          "Average Subtotal Group By Date", 
          "getprofits"
        ];
      } else if (this.selectedSections === "Infomation") {
        this.subTables = [
          "getproduct_info", 
          "getcategories_info",
          "getavg_price_in_categories"
        ]
      } else if (this.selectedSections === "Others") {
        this.subTables = [
          "getprice_difference",
        ]
      }
      this.subSelection = this.subTables[0];
    },
    fetchData() {
      if (this.selectedSections === "Quantity Sold") {
        if (this.subSelection === "Group By Products") {
          this.getSalesQuantityProducts();
        } else if (this.subSelection === "Group By Categories"){
          this.getSalesQuantityCategories();
        } else if (this.subSelection === "Transactions Information"){
          this.getSalesQuantity();
        }
      } else if(this.selectedSections === "Inventory"){
        if (this.subSelection === "Stock In Warehouse") {
          this.getStockInWarehouse()
        } else if (this.subSelection === "Product Out Of Stock"){
          this.getProductOutOfStock()
        } else if (this.subSelection === "Product Stock"){
          this.getProductStock()
        }
      } else if(this.selectedSections === "Revenue"){
        if(this.subSelection === "Cumulative Revenue Group By Date"){
          this.getCumulativeRevenueInDate();
        } else if(this.subSelection === "Average Subtotal Group By Date"){
          this.getAvgSubtotalWindow()
        } else if(this.subSelection === "getprofits"){
          this.getprofits()
        }
      } else if (this.selectedSections === "Popular Ranking") {
        if (this.subSelection === "getmost_popular_categories") {
          this.getmost_popular_categories()
        } else if (this.subSelection === "getmost_popular_supplier"){
          this.getmost_popular_supplier()
        } else if (this.subSelection === "getrank1_product_in_categories"){
          this.getrank1_product_in_categories()
        } else if (this.subSelection === "getbuyer_ranking"){
          this.getbuyer_ranking()
        }
      } else if (this.selectedSections === "Infomation") {
        if (this.subSelection === "getproduct_info") {
          this.getproduct_info()
        } else if (this.subSelection === "getcategories_info"){
          this.getcategories_info()
        } else if(this.subSelection === "getavg_price_in_categories"){
          this.getavg_price_in_categories()
        }
      } else if (this.selectedSections === "Others") {
        if (this.subSelection === "getprice_difference") {
          this.getprice_difference()
        }
      } else {
        this.data.headers = ['Not available']
      }
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    getSalesQuantity(){
      const body = {
        start_date: "2022-01-01",
        end_date: "2023-12-31",
      }
      axios.post("http://127.0.0.1:8000/advanced/quantity_sold", body)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
        window.alert("Error: Fail");
      });
    },
    getSalesQuantityCategories(){
      const NTILENum = 4;
      axios.get(`http://127.0.0.1:8000/advanced/quantity_sold/categories/${NTILENum}`)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
        window.alert("Error: Fail");
      });
    },
    getSalesQuantityProducts(){
      const NTILENum = 3;
      axios.get(`http://127.0.0.1:8000/advanced/quantity_sold/products/${NTILENum}`)
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
        window.alert("Error: Fail");
      });
    },
    getCumulativeRevenueInDate(){
      axios.get("http://127.0.0.1:8000/advanced/cumulative_revenue_in_date/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
        window.alert("Error: Fail");
      });
    },
    getAvgSubtotalWindow(){
      axios.get("http://127.0.0.1:8000/advanced/avg_subtotal_window")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
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
        window.alert("Error: Fail");
      });
    },
    getProductStock(){
      axios.get("http://127.0.0.1:8000/advanced/product_stock/")
      .then((response) => {
        // Handle the response data
        this.data = response.data;
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error:', error);
        window.alert("Error: Fail");
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
  width: 200px;
  margin-top: 20px;
}
.choose-area .table_radio{
  text-align: left;
}
.choose-area .table_radio label{
  padding: 20px;
  height: 50px;
  width: 200px;
}
.choose-area .table_radio label:hover{
  cursor: pointer;
}
.selected-label{
  background-color: burlywood;
  font-weight: 900;
}
</style>
