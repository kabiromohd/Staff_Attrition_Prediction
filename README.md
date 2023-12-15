# Staff_Attrition_Prediction
## DatatalksClub ML Zoomcamp Capstone Project 1
## Objectives of Capstone Project:
- Find a dataset
- Explore and prepare the data
- Train the best model
- Export the notebook into a script
- Put model into a web service
- Deploy model locally with Docker
- Deploy to the cloud
  
### Find a Dataset
### Overview and Objective of Project

In the dynamic world of business, understanding and predicting employee attribution is crucial. This project harness the power of data and AI to forecast and analyze employee attribution trends. We will have the opportunity to dive deep into HR analytics and explore the factors that influence employee turnover. 

The data for this project is from [Dataset Link](https://www.kaggle.com/competitions/oht-ibadan-bootcamp-capstone-open-house/data)

The aim of the project is to develop a predictive model that provide insights into employee retention, identify patterns, and contribute to strategic talent management.

### Explore and prepare the data
Exploration of the data was done via *ML_Zoomcamp_Attrition_Pred_Proj.ipynb* jupyter notebook file
- Explore data
  - Checked the Data Structure and columns
  - Checked the numbers of features and observations in the data
  - Checked the inconsistency in column names and corrected
  - Check the correlation of the features to the target variable (attrition)
- prepare data
  - Checked for missing values
  - Checked for outliers
  - Checked for Duplicates
- train data
  - Catergorical variables were encoded using the DictVectorizer library.
  - trained best model using the random forest regressor after ascertaining it to produce the best model with hyper parameters via *Train_model.py* script.
