<h1>Egyptian Housing Price Predictor 🏠🇪🇬 </h1><br>

This project aims to predict residential property prices in Egypt using data scraped from Aqarmap.<br>
The project covers the entire machine learning pipeline, from raw data merging and cleaning to interactive model deployment using Python widgets.<br>

<h2>📁 Project Structure</h2><br>

01_data_preprocessing.ipynb: Handles the merging of multiple raw CSV files, data cleaning (handling nulls, correcting types), and basic feature engineering.<br>

02_eda.ipynb: Exploratory Data Analysis including geographic distribution (Lat/Lon), price density analysis, and Arabic text reshaping for visualizations.<br>

03_model.ipynb: Machine learning pipeline using Ridge Regression, OneHotEncoding, and an interactive prediction dashboard.<br>

<h2>📊 Dataset Overview:</h2><br>

The dataset contains listings with the following features:<br>
Location: Governate, City, and Neighborhood.Specs: Area ($m^2$), Number of Rooms, Bathrooms, and Floor level.Condition: Finishing type (e.g., Ultra Super Lux, Semi-finished).Target: Price (EGP).<br>

<h2>🚀 Key Features</h2> <br>

Geospatial Visualization: Maps showing price distribution across Egyptian governates.<br>
<img width="300" height="594" alt="image" src="https://github.com/user-attachments/assets/fb936f13-6f6e-4b1e-a108-98189fd78c4a" />


Arabic Support: Custom integration with arabic_reshaper to ensure city names render correctly in plots.<br>

Interactive Predictor: A built-in dashboard in the modeling notebook that allows users to input house specs and get an instant price estimate.<br>
<img width="300" height="421" alt="image" src="https://github.com/user-attachments/assets/a5112db9-016d-4bc2-8c7c-b0a133d86bea" />

## Live Demo
Try the app here: [Housing Price Predictor](https://housing-project-um9mec2vgxdn6jmunnxt9p.streamlit.app/)
