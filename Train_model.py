#!/usr/bin/env python
# coding: utf-8

# Load Required Libraries
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import seaborn as sns
import pickle
from IPython.display import display

import matplotlib.pyplot as plt
from xgboost import XGBClassifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

get_ipython().run_line_magic('matplotlib', 'inline')


# Functions used for Project

def wrangle(filename):
    df = pd.read_csv(filename, index_col = "id")

    # Delete feature with high corelation
    del df["EmployeeCount"]
    del df["StandardHours"]
    return df

def prepare_data_split(df, test_size, random_state, target_feature):
    '''
    Function Splits a dataset(df) in the Train/test  dataset

    return the train, Test dataset
    '''
    df_train, df_test = train_test_split(df, test_size= test_size, random_state=random_state)

    df_train = df_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)

    y_train = df_train[target_feature].values
    y_test = df_test[target_feature].values

    del df_train[target_feature]
    del df_test[target_feature]

    print(f"Length of X_train: {len(df_train)}, Length of X_test: {len(df_test)}")
    print(f"Length of y_train: {len(y_train)}, Length of y_test: {len(y_test)}")
    return df_train, y_train, df_test, y_test


def outliers(X, y):
    # Automatically detect ouliers and remove
    lof = LocalOutlierFactor()
    outliers = lof.fit_predict(X)

    # select all rows that are not outliers
    mask = outliers != -1
    X_train, y_train = X[mask], y[mask]
    return X_train, y_train


def cat_encoder(X_train, X_val):
    # Applying the DictVectorizer

    dv = DictVectorizer(sparse = False)

    train_dicts = X_train.to_dict(orient='records')
    X_train = dv.fit_transform(train_dicts)

    val_dicts = X_val.to_dict(orient='records')
    X_val = dv.transform(val_dicts)
        
    #Save Encoder to disk
    with open("dicv.pkl", "wb") as f:
        pickle.dump(dv, f)
    return X_train, X_val

def min_max_scaler(X_train, X_val):
    # scale the dataset
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    return X_train, X_val


# Load Data

filename = "train.csv"
df = wrangle(filename)

# Setup Validation framework
test_size = 0.2
random_state = 42
target_feature = "Attrition"
X_train, y_train, X_val, y_val = prepare_data_split(df, test_size, random_state, target_feature)

# Apply Encoder to categorical features
X_train, X_val = cat_encoder(X_train, X_val)

# Auto Eliminate Outliers from Training dataset
X_train, y_train = outliers(X_train, y_train)

# Scale the data using MinMaxScaler
X_train, X_val = min_max_scaler(X_train, X_val)


# ### Gradient Boosting Classifier Model

print("Training Gradient Boosting Classifier")

model = GradientBoostingClassifier(max_depth = 5, max_features = 'log2', n_estimators = 90, random_state = 42)

model.fit(X_train, y_train)

# Save the trained model

with open("best_model_capst.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Trained and saved as best_model_capst.pkl"