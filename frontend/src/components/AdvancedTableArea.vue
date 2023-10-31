<template>
  <div class="advanced-table-area">

    <div class="side-nav"> 
      <h3>choose one table:</h3>
      <div class="choose-area">
        <div class="table_radio" v-for="(item,index) in tables" :key="index">
          <input v-model="selection" type="radio" name="tables" :value="item" :id="item+index" >
          <label :for="item+index">{{item}}</label>
        </div>
      </div>
    </div>

    <div class="result">
      <h1>
        <span v-if="selection">{{capitalizeFirstLetter(selection)}}</span>
      </h1>

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

export default {
  name: 'TableArea',
  components:{
    Table,
  },
  data() {
    return {
      selection: "",
      tables: [
        "Count the number of products purchased in each category",
        "Analyze NTile distribution of total purchases for each product in descending order",
        "Rank the percentage of products bought from suppliers in descending order",
        "Create a table displaying the quantity of products in each category sold by each supplier",
        "Count different categories sold per supplier",
        "Create a table displaying revenues, costs, and profits for each year",
        "Create a table displaying revenues, costs, and profits for each year and month",
        "Display the average costs, profits, and revenues for each month",
        "List the top 5 suppliers by the number of products they supply",
        "Find the product with the highest price",
        "List products that are out of stock",
        "Find the most recent transaction for each product",
        "List products in a specific category (e.g., 'Electronics')",
        "List all transactions made by a specific buyer",
        "Calculate the average price of products in each category",
        "List the products with their suppliers and manufacturers",
        "Calculate the total quantity of a specific product in each warehouse",
        "List the most popular product categories (top 3) by the number of products sold",
        "Calculate the running total of quantities in inventory over time (OLAP)",
        "Calculate the running total of inventory value over time",
        "Find products with the highest inventory value using a CTE",
        "Find the Moving Average of Product Prices over a 3-Month Window",
        "Calculate the Cumulative Quantity Sold by Buyer Over Time",
        "Calculate the Difference in Price Between Current and Previous Transaction",
        "Find the Product with the Highest Price in Each Category",
        "Find the Average Price of Products in Each Category Along with the Category's Highest and Lowest Prices",
        "Determine the Number of Transactions Occurring Each Month",
        "Find the First and Last Transaction Dates for Each Product",
        "Calculate the total cost of a purchase for a specific product and quantity"
      ],

      test_header:["CategoriesID","CategoriesName","Total_Products_Purchased"],
      test:[
        {"CategoriesID": 1, "CategoriesName": "CategoriesName", "Total_Products_Purchased":  30},
        {"CategoriesID": 2, "CategoriesName": "CategoriesName2", "Total_Products_Purchased":  60},
      ],
    };
  },
  computed: {
    headers() {
      return this.test_header;
    },
    contents() {
      return this.test;
    }
  },
  mounted(){
    if (this.tables) {
      this.selection = this.tables[0]
    }
  },
  methods:{
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
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
  max-height: calc(100vh - 178px);
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
  margin-left: 5px;
}
</style>
