#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:6090/predict'

staff = {"Age": 30,
         "BusinessTravel": "Travel_Rarely",
         "DailyRate": 1392,
         "Department": "Research & Development",
         "DistanceFromHome": 7,
         "Education": 4,
         "EducationField": "Life Sciences",
         "EnvironmentSatisfaction": 2,
         "Gender": "Male",
         "HourlyRate": 77,
         "JobInvolvement": 4,
         "JobLevel": 1,
         "JobRole": "Research Scientist",
         "JobSatisfaction": 2,
         "MaritalStatus": "Divorced",
         "MonthlyIncome": 2413,
         "MonthlyRate": 26314,
         "NumCompaniesWorked": 1,
         "Over18": "Y",
         "OverTime": "Yes",
         "PercentSalaryHike": 18,
         "PerformanceRating": 3,
         "RelationshipSatisfaction": 3,
         "StockOptionLevel": 1,
         "TotalWorkingYears": 10,
         "TrainingTimesLastYear": 3,
         "WorkLifeBalance": 2,
         "YearsAtCompany": 10,
         "YearsInCurrentRole": 7,
         "YearsSinceLastPromotion": 0,
         "YearsWithCurrManager": 1
        }

response = requests.post(url, json=staff)


if response.status_code == 200:
    # Successful response
    try:
        json_response = response.json()
        print(f"Probability for Attrition of staff: {json_response['Probability_Attrition: ']}")
        print()
        print(f"Determined Attrition status: {json_response['Attrition_Status']}")
    except requests.exceptions.JSONDecodeError:
        print("Response is not a valid JSON.")
else:
    # Handle non-200 status code
    print("Request failed with status code:", response.status_code)
