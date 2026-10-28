# 🍔 Food Delivery Data Analysis Project

## 📌 Project Overview

The **Food Delivery Analysis Project** is a data analytics project developed to analyze food delivery operations using SQL, Python, and Streamlit.

The project involves creating database tables in SQL, importing and cleaning data using Python, connecting Python to the SQL database, and performing analysis on orders, customers, and delivery data.

A web application was developed using Streamlit to present the analyzed data in an interactive and user-friendly format.

The main objective of this project is to transform raw food delivery data into meaningful insights that can help understand customer behavior, order trends, and delivery operations.

## 🎯 Project Objectives

- Create and manage a food delivery database using SQL.
- Import data into Python for processing and analysis.
- Clean raw data to improve data quality and consistency.
- Establish a connection between Python and the SQL database.
- Analyze order, customer, and delivery data.
- Develop a web application using Streamlit.
- Display analysis results through a simple and interactive interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| SQL / MySQL | Database creation, table management, and data storage |
| Python | Data processing, cleaning, and analysis |
| Pandas | Data manipulation and analysis |
| SQL Connector | Connecting Python to the SQL database |
| Streamlit | Building the interactive web application |
| Git & GitHub | Version control and project sharing |

## 🔄 Project Workflow

The project follows these steps:

### 1. Database Creation Using SQL
- Created the required tables for the food delivery system.
- Structured the data to store customer, restaurant, order, and delivery information.
- Used SQL to manage and retrieve data from the database.

### 2. Data Import and Cleaning Using Python
- Imported data into Python.
- Examined the datasets for data quality issues.
- Cleaned and processed the data.
- Prepared the datasets for further analysis.

### 3. Database Connection
- Connected Python to the SQL database.
- Retrieved data from the database for analysis.
- Integrated SQL data with Python-based data processing.

### 4. Data Analysis
Performed analysis across three major areas:

**📦 Order Analysis**
- Examined order-related data.
- Explored order trends and patterns.
- Analyzed relevant order information.

**👥 Customer Analysis**
- Examined customer information.
- Explored customer-related patterns.
- Analyzed the available customer data.

**🚚 Delivery Analysis**
- Examined delivery-related information.
- Explored delivery status and operational patterns.
- Analyzed delivery data to understand delivery operations.

### 5. Web Application Development
- Built a web application using Streamlit.
- Integrated the analysis results into the application.
- Displayed the available data and analysis on a single web interface.
- Made the results easier to explore and understand.

## 🖥️ Application Features

- **Order Analysis:** Explore order-related data and trends.
- **Customer Analysis:** View and examine customer information.
- **Delivery Analysis:** Explore delivery-related data.
- **Data Visualization:** Present analysis results in a user-friendly format.
- **Interactive Web Interface:** Access the project through a Streamlit application.

*Note: The features displayed depend on the analyses and visualizations implemented in the application.*

## 📂 Project Structure

The following is an example of how the project files can be organized. Update the names to match your actual project structure.

```text
Food_delivery_project/
│
├── app.py
├── cleaning_data.py
├── customers_Analysis.py
├── orders_Analysis.py
├── delivery_Analysis.py
├── requirements.txt
├── README.md
│
├── Data_SQL/
│   └── CSV data files
│
└── Other project files
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### Prerequisites

Make sure you have installed:

- Python 3
- MySQL Server
- MySQL Workbench (optional, for database management)
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd Food_delivery_project
```

### Step 2: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

If a `requirements.txt` file is available, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your project. For example:

```bash
pip install pandas sqlalchemy mysql-connector-python streamlit
```

Install any additional libraries used in your Python scripts.

### Step 4: Configure the Database

1. Start your MySQL server.
2. Create the required database and tables.
3. Import or insert the project data.
4. Configure the database connection in your Python code.

**Important:** Use your own database credentials and configuration. Never upload passwords or other sensitive credentials to GitHub.

### Step 5: Run the Data Cleaning Script

If your project uses `cleaning_data.py` to prepare the data, run:

```bash
python cleaning_data.py
```

Skip this step if your data has already been prepared and the application does not require the script to run again.

### Step 6: Launch the Streamlit Application

Run the following command from the project directory:

```bash
streamlit run app.py
```

Streamlit will provide a local address where you can open and explore the application in your web browser.

## 📊 Key Learning Outcomes

Through this project, I gained practical experience in:

- SQL database creation and management.
- Python-based data cleaning and preprocessing.
- Connecting Python with a relational database.
- Using Pandas for data manipulation.
- Analyzing customer, order, and delivery datasets.
- Developing web applications using Streamlit.
- Integrating multiple technologies into a complete data analytics project.
- Presenting data analysis through a user-friendly interface.

## 🚀 Future Enhancements

Potential improvements for this project include:

- Adding interactive charts and KPI cards.
- Implementing date, customer, and delivery-status filters.
- Adding more advanced SQL queries.
- Developing deeper customer behavior analysis.
- Adding delivery performance KPIs.
- Improving dashboard design and usability.
- Deploying the Streamlit application online.
- Automating data updates from the SQL database.

## 👩‍💻 Author

**Your Name**

Aspiring Data Analyst | B.Com. (Hons.) Student

**Skills Demonstrated:** SQL | Python | Pandas | MySQL | Streamlit | Data Analysis

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.