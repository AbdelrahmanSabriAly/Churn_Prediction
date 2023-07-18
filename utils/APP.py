import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin

#Helper function

def PREDICT(List,X,model):
    x = np.zeros(len(X.columns))
    counter = 0
    for i in List:
        x[counter] = i
        counter+=1
        
    return model.predict([x])[0]

def show_res(Input,X,model,tab_name):
    res = PREDICT(Input,X,model)

    if res == 0:
        tab_name.error("The customer will likely leave our bank")
    else:
        tab_name.success("The customer will likely stay in out bank")





def show_APP(tab_name,df,categorical_cols,model):
    X = df.drop("Exited",axis = 1)
    X_encoded = X.copy()
    for col in categorical_cols:

        # Example data with categorical labels
        labels = X[col]

        # Step 1: Create a LabelEncoder instance
        label_encoder = LabelEncoder()

        # Step 2: Fit the encoder on the labels to learn the mapping of labels to integers
        label_encoder.fit(labels)

        # Step 3: Transform the labels into numerical format
        X_encoded[col] = label_encoder.transform(labels)


    n = len(categorical_cols)  # Number of dictionaries in the list
    map_list = [{} for _ in range(n)] 

    for i in range(len(categorical_cols)):
        for j in range (len(df[categorical_cols[i]])):
            map_list[i][df[categorical_cols[i]][j]] = X_encoded[categorical_cols[i]][j]

    CreditScore = tab_name.slider('Enter the Credit Score', 100, 1000)

    Geography = tab_name.radio('Select the Geography', ['France', 'Spain','Germany'])
    Geography = map_list[0][Geography]

    Gender = tab_name.radio('Select the Gender', ['Male', 'Female'])
    Gender = map_list[1][Gender]

    Age = tab_name.slider('Enter the Credit Score', 10, 100)

    Tenure = tab_name.selectbox("Select the Tenure", [0,1,2,3,4,5,6,7,8,9,10])

    Balance = tab_name.slider('Enter the Balance', 0, 10000000)

    NumOfProducts = tab_name.slider('Enter the Number of products', 1, 10)

    HasCrCard = tab_name.radio('Does he/she have a Credit Card?', ['Yes', 'No'])
    if HasCrCard == 'Yes':
        HasCrCard = 1
    else:
        HasCrCard = 0

    IsActiveMember = tab_name.radio('Is he/she have an Active member?', ['Yes', 'No'])
    if IsActiveMember == 'Yes':
        IsActiveMember = 1
    else:
        IsActiveMember = 0

    EstimatedSalary = tab_name.slider('Enter the Estimated Salary', 0, 10000000)

    Input = [CreditScore,Geography,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]

    predict_button = tab_name.button("Predict!")

    if predict_button:
        show_res(Input,X,model,tab_name)

