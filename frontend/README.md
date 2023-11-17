# Frontend Instructions

## Part 1: Project Setup

### step 1:
- Run the following command to install dependencies:
  ```
  npm install
  ```

- Alternatively, you can install Node.js from this link.
https://nodejs.org/en/download 

### step 2: 
- Run the following command to compile and enable hot-reloading during development:

  ```
  npm run serve
  ```
- Alternatively, You can run this command on Windows PowerShell.

### step 3:
- Open the link provided in your command line, for example: http://localhost:8080/.
- You will be directed to the main website UI.

### step 4:
- Go to "frontend -> src -> App.vue". App.vue serves as the main page for our project.
- Explore other components in "frontend -> src -> components".

## Part 2: Frontend code Introduction

This Vue component is designed to create a dynamic and editable table, providing functionality for displaying, adding, updating, and deleting rows. The component is flexible and can handle different data structures based on the passed props. We will take "Table. vue" as an example.

### Project Structure
- src: The source directory containing the main application code.
- components: Vue components for various functionalities.
- assets: Static assets such as images or fonts.
- views: Higher-level Vue components representing different views.
- router: Manages the application's routing configuration.
- store: Implements state management using Vuex.
- styles: Global styles and CSS files.


### Props
- headers: An array of strings representing the column headers of the table.
- contents: An array of objects representing the data for each row in the table.
- editorOn: A Boolean to toggle edit mode on the table.
- selectedTable: A String indicating the currently selected table type.

### Data
- newContent: An object to hold the data for a new row being added.
- nextID: A string to hold the next ID when adding a new row.

### Methods
- addItem(newContent): Adds a new row to the table.
- dropItem(item, index): Deletes a row from the table.
- updateItem(item): Updates an existing row in the table.

### Usage
- Display Table: The table initially displays the data passed through the contents prop with headers from the headers prop.
- Edit Mode: When editorOn is true, each row becomes editable with text inputs and action buttons for updating or deleting.
- Adding New Rows: Depending on the selectedTable value, different input fields are displayed for adding a new row.
- Updating and Deleting Rows: Each row has an "Update" and "Delete" button for performing respective actions.

Our frontend is structured for ease of use, flexibility, and an enhanced user experience. The dynamic table component offers seamless data management and interaction capabilities.
