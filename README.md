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

The data for this project is from [Dataset Link](https://www.kaggle.com/competitions/bct-data-summit/data)

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
  - trained best model using the Gradient Boosting Classifier model after ascertaining it to produce the best model with hyper parameters via *Train_model.py* script.

 ### Environment Setup
- Setup Pipenv Virtual Environment, by opening Cli on your system and execute the below:
  
```
pip install pipenv
```

- install the following:
  - Gunicorn
  - flask
  - numpy
  - scikit-learn version "1.3.2"
  - requests

- Execute the following in the cli:

Step 1
```
pipenv shell
```

Step 2
```
pipenv install gunicorn flask numpy scikit-learn=="1.3.2" requests
```

- Get copies of the project and dependencies, you can clone the repo.
- The copied files should be placed in the virtual environment folder after being cloned via below command.

```
git clone https://github.com/kabiromohd/Staff_Attrition_Prediction.git
```

### Model deployment to web services
flask was used for web deployment via *predict.py* script. Test the flask web deployment execute the following:

NB: You need to be in the folder where the environment was setup in my own case "c:\midterm"

Step 1
```
pipenv shell
```

Step 2
```
python predict.py
```
You get the below screenshot:

![run predict](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/742485a2-1f4a-40f2-ac6c-ac2d0068fe10)

To test the flask web services deployment a data point has been created in *predict_test.py* file.

NB: You need to be in the folder where the environment was setup in my own case "c:\midterm"

Open another fresh Cli and run the following:

Step 1
```
pipenv shell
```

Step 2
```
python predict_test.py
```
You get the below screenshot:

![run predict test](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/2014c241-82f9-4e58-aff5-a194a9ae2f36)

