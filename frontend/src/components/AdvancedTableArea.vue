<template>
  <div class="advanced-table-area">
    <div class="txt">
      <div class="side-nav"> 
        <div class="choose-area">
          <div class="table_radio" v-for="(item,index) in sections" :key="index">
            <input v-model="selectedSections" type="radio" name="sections" :value="item" :id="item+index" class="d-none">
            <label class="sections-label" :for="item+index" :class="{ 'selected-label': selectedSections === item }">{{item}}</label>
            <div class="subTable-area" v-if="selectedSections === item">
              <div v-for="(table,index) in subTables" :key="index">
                <input v-model="subSelection" type="radio" name="subTables" :value="table" :id="table+index" class="d-none">
                <label :for="table+index" class="subTable-label" :class="{ 'subselected-label': subSelection === table }">{{table}}</label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="result">
        <h1>
          <span v-if="subSelection">{{capitalizeFirstLetter(subSelection)}}</span>
        </h1>

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
        "Ranking",
        "Stock",
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
          "Quantity By Products",
          "Quantity By Categories"
        ];
      } else if (this.selectedSections === "Ranking") {
        this.subTables = [
          "Buyer Ranking",
          "Sales Ranking",
          "No.1 Selling Product in Each Category (excluding products with a price <= 50)"
        ]
      } else if (this.selectedSections === "Stock") {
        this.subTables = [
          "Stock In Warehouse", 
          "Product Stock", 
          "Product Out Of Stock"
        ];
      } else if (this.selectedSections === "Revenue") {
        this.subTables = [
          "Cumulative Revenue Group By Date",
          "Average Subtotal Group By Date", 
          "Profits For Each Month",
          "State Revenue",
          "Total Revenue",
          "Search Profits by Category"
        ];
      } else if (this.selectedSections === "Infomation") {
        this.subTables = [
          "Product Information", 
          "Buyer Information",
          "Transactions Information",
          "Price Infomation In Each Categories"
        ]
      } else if (this.selectedSections === "Others") {
        this.subTables = [
          "Price Difference",
        ]
      }
      this.subSelection = this.subTables[0];
    },
    fetchData() {
      if (this.selectedSections === "Quantity Sold") {
        if (this.subSelection === "Quantity By Products") {
          this.getSalesQuantityProducts();
        } else if (this.subSelection === "Quantity By Categories"){
          this.getSalesQuantityCategories();
        }
      } else if(this.selectedSections === "Stock"){
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
        } else if(this.subSelection === "Profits For Each Month"){
          this.getProfitsPerMonth()
        } else if (this.subSelection === "State Revenue"){
          this.getStateRevenue()
        } else if(this.subSelection === "Total Revenue"){
          this.getTotalRevenue()
        } else if (this.subSelection === "Search Profits by Category"){
          this.getCategoriesProfits()
        }
      } else if (this.selectedSections === "Ranking") {
        if (this.subSelection === "No.1 Selling Product in Each Category (excluding products with a price <= 50)"){
          this.getNo1ProductInCategories()
        } else if (this.subSelection === "Buyer Ranking"){
          this.getBuyerRanking()
        } else if(this.subSelection === "Sales Ranking") {
          this.getSalesRank()
        }  
      } else if (this.selectedSections === "Infomation") {
        if (this.subSelection === "Product Information") {
          this.getProductInfo()
        } else if(this.subSelection === "Price Infomation In Each Categories"){
          this.getPriceInfoInCategories()
        } else if (this.subSelection === "Transactions Information"){
          this.getSalesQuantity();
        } else if (this.subSelection === "Buyer Information"){
          this.getBuyerInfo()
        }
      } else if (this.selectedSections === "Others") {
        if (this.subSelection === "Price Difference") {
          this.getPriceDifference()
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
    getBuyerRanking(){
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
    getPriceDifference(){
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
    getNo1ProductInCategories(){
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
    getStateRevenue(){
      axios.get("http://127.0.0.1:8000/advanced/state_revenue/")
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
    getProductInfo(){
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
    getSalesRank(){
      axios.get("http://127.0.0.1:8000/advanced/sales_rank/")
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
    getProfitsPerMonth(){
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
    getBuyerInfo(){
      axios.get("http://127.0.0.1:8000/advanced/buyer_info/")
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
    getPriceInfoInCategories(){
      axios.get("http://127.0.0.1:8000/advanced/price_info_in_categories/")
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
    getTotalRevenue(){
      axios.get("http://127.0.0.1:8000/advanced/total_revenue/")
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
    getCategoriesProfits(){
      const categoriesName = "Car";
      axios.get(`http://127.0.0.1:8000/advanced/categories_profits/${categoriesName}`)
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
  width: 230px;
  margin-top: 20px;
}
.choose-area .table_radio{
  text-align: left;
}
.choose-area .table_radio .sections-label{
  padding: 20px;
  height: 50px;
  width: 230px;
}
.choose-area .table_radio label:hover{
  cursor: pointer;
}
.selected-label{
  background-color: burlywood;
  font-weight: 900;
}
.subTable-area{
  visibility: 0;
  transition: all 0.8s;
}
.choose-area .table_radio .subTable-area .subTable-label{
  background-color: antiquewhite;
  border-top: 1px dotted #aaa;
  padding: 10px;
  padding-left: 25px;
  height: 100%;
  width: 100%;
  color: #aaa;
}
.choose-area .table_radio .subTable-area .subTable-label:hover{
  color: #2c3e50;
}
.choose-area .table_radio .subTable-area .subselected-label{
  color: #2c3e50;
}
</style>
