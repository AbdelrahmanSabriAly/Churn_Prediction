import streamlit as st

def ABOUT(tab_name):
    tab_name.subheader("Bank Customer Churn Prediction based on the following dataset:")
    tab_name.markdown("[Bank Customer Dataset for Churn prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)")
    tab_name.markdown(
    """
    ### In this project:
    - An exploratory data analysis is done (both univariate and bivariate analysis).
    - GridSearchCV is used to train multiple classification algorithms, fine tune them and find the best algorithm for the project.
    - Gradient Boosting Classifier achieved the highest score on the test data (86.5%)
    - Streamlit is used for deployment.

    """
    ,unsafe_allow_html=True)

    tab_name.write("The link of the github repository is the following :")
    tab_name.markdown("[GitHub Repo](https://github.com/AbdelrahmanSabriAly/Churn_Prediction.git)")
