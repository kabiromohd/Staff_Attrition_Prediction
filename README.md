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
- NB: All Command Line interface (Cli) commands need to be excecuted in the folder where the Virtual Environment was created and setup - Virtual Environment for this project was setup in folder "c:\midterm".
  
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

- To copies of the project and dependencies, clone the repo.
- The copied files should be placed in the virtual environment folder after being cloned via below command.

  ```
  git clone https://github.com/kabiromohd/Staff_Attrition_Prediction.git
  ```

### Model deployment to web services
- Flask was used for web deployment via *predict.py* script. To test the flask web deployment execute the following:

  Step 1
  ```
  pipenv shell
  ```

  Step 2
  ```
  python predict.py
  ```

- Below screenshot illustrates output:

![run predict](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/742485a2-1f4a-40f2-ac6c-ac2d0068fe10)

- To test the flask web services deployment a data point has been created in *predict_test.py* file.

- Open another fresh Cli and run the following:

  Step 1
  ```
  pipenv shell
  ```

  Step 2
  ```
  python predict_test.py
  ```

- Below screenshot illustrates the output:

![run predict test](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/2014c241-82f9-4e58-aff5-a194a9ae2f36)


### Deploy model locally with Docker
- Deploy Flask web services to Docker locally by following these steps.
  
  - Install Docker desktop and need to be running before building image.
  - Create an account on docker web login [Docker Web](https://hub.docker.com).
  - Creating an account on Docker enables setting up of Docker repository which can be used to push the docker image created locally.
  - Docker repo created for the purpose of this project is *"kabiromohd/data_science"*.
  - Docker repository was created to enable getting URL for the capstone1 image.

- To create the project docker image:
  
  - Create a docker repo, which in my case "kabiromohd/data_science".
  - You can create the Docker repo from the web sign in interface of docker [Docker Web](https://hub.docker.com)

  ```
  pipenv shell
  ```

  - Create docker image by running the following:

  ```
  docker build -t kabiromohd/data_science:capstone1 .
  ```

  - followed by this docker command which runs the docker image created

  ```
  docker run -it --rm -p 6090:6090 kabiromohd/data_science:capstone1
  ```

  - If the two commands run successfully below screenshot will be seen:

![Docker Deployment](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/a7f86a23-a33f-4e48-b2dc-0fa7d8ec4279)

- To test the local Docker deployment:
  - Open another created virtual environment Cli and run below command to see prediction.
  - The output should be the same as a the flask web services deployment.

  ```
  pipenv shell
  ```

  - Note: *predict_test.py* has already prepared with data point to test the model deployed locally on docker

  Run below command. 

  ```
  python predict_test.py
  ```

This ends the local deployment to docker.

### Deploy docker image to the cloud

- For cloud deployment [Render](render.com) was used.
- User account needs to be created on Render
- To deploy the docker image to cloud, open a Cli and run the following commands:

```
pipenv shell
```

- Push the docker image created above to the repo created with the following command:

```
docker push kabiromohd/data_science:capstone1
```

- The image pushed to docker web will appear as in below screenshot

![Docker Web](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/4fa96c59-5927-4a6b-9aba-f97cf2ab622b)

- Copy the docker image URL to render from the docker repo

![Render Interface](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/a636a9f0-7d24-4c23-91c1-91990b6cb873)


- Deploy docker image to Render cloud service. See below screenshot for the output of deployment
  
![Render Deployment](https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/5347603c-8b89-47e6-a70d-c61edb297520)


### Deployment Link

[My Capstone 1 Deployment Link from Render](https://ml-zoomcamp-capstone1.onrender.com)

### To interact with the docker image deployed to Render cloud Services

- copy the render deployment link and place in the *predict_render.py* script as "host".
- *predict_render.py* also has already prepared data point to be used to test the model deployed to cloud.
- for this project, the deployment link has already been provided in the *predict_render.py* script. It can be executed as illustrated below:
  
- Open created Virtual Environment Cli and run the following: 

  ```
  pipenv shell
  ```

  followed by:
  
  ```
  python predict_render.py
  ```
  
### Video illustration of Cloud Deployment test
See illustration video below:

https://github.com/kabiromohd/Staff_Attrition_Prediction/assets/121871052/6e9473a3-e56b-4524-950d-7ff07e757541
