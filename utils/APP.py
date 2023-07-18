import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Helper function to predict churn
def predict_churn(features, X, model):
    """
    Predicts churn for a given set of features using the provided model.

    Parameters:
        features (list): List of input features.
        X (pandas.DataFrame): DataFrame containing the dataset without the target column.
        model (sklearn.base.BaseEstimator): The trained classification model.

    Returns:
        int: Prediction label (0 for customer leaving, 1 for customer staying).
    """
    x = np.zeros(len(X.columns))
    for i, value in enumerate(features):
        x[i] = value
    return model.predict([x])[0]

# Display prediction result
def show_prediction_result(input_features, X, model, tab_name):
    """
    Displays the prediction result for the given input features.

    Parameters:
        input_features (list): List of input features.
        X (pandas.DataFrame): DataFrame containing the dataset without the target column.
        model (sklearn.base.BaseEstimator): The trained classification model.
        tab_name (streamlit.DeltaGenerator): Streamlit tab to display the content.
    """
    prediction_result = predict_churn(input_features, X, model)

    if prediction_result == 0:
        tab_name.error("The customer will likely leave our bank")
    else:
        tab_name.success("The customer will likely stay in our bank")

def show_app(tab_name, df, categorical_cols, model):
    """
    Displays the Streamlit app for predicting customer churn.

    Parameters:
        tab_name (streamlit.DeltaGenerator): Streamlit tab to display the content.
        df (pandas.DataFrame): DataFrame containing the dataset with target column "Exited".
        categorical_cols (list): List of categorical columns in the dataset.
        model (sklearn.base.BaseEstimator): The trained classification model.
    """
    X = df.drop("Exited", axis=1)
    X_encoded = X.copy()

    # Convert categorical features to numerical using LabelEncoder
    for col in categorical_cols:
        label_encoder = LabelEncoder()
        X_encoded[col] = label_encoder.fit_transform(X[col])

    # Create a dictionary for mapping categorical values to numerical labels
    mapping_dict = {col: {val: X_encoded[col][idx] for idx, val in enumerate(df[col])} for col in categorical_cols}

    # Input features
    CreditScore = tab_name.slider('Enter the Credit Score', 100, 1000)
    Geography = tab_name.radio('Select the Geography', ['France', 'Spain', 'Germany'])
    Geography = mapping_dict['Geography'][Geography]

    Gender = tab_name.radio('Select the Gender', ['Male', 'Female'])
    Gender = mapping_dict['Gender'][Gender]

    Age = tab_name.slider('Enter the Age', 10, 100)
    Tenure = tab_name.selectbox("Select the Tenure", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Balance = tab_name.slider('Enter the Balance', 0, 10000000)
    NumOfProducts = tab_name.slider('Enter the Number of products', 1, 10)
    HasCrCard = tab_name.radio('Does he/she have a Credit Card?', ['Yes', 'No'])
    HasCrCard = 1 if HasCrCard == 'Yes' else 0

    IsActiveMember = tab_name.radio('Is he/she have an Active member?', ['Yes', 'No'])
    IsActiveMember = 1 if IsActiveMember == 'Yes' else 0

    EstimatedSalary = tab_name.slider('Enter the Estimated Salary', 0, 10000000)

    input_features = [CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember,
                      EstimatedSalary]

    predict_button = tab_name.button("Predict!")

    if predict_button:
        show_prediction_result(input_features, X, model, tab_name)
