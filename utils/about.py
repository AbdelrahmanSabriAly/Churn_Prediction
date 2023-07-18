import streamlit as st

def display_about_info(tab_name):
    """
    Displays information about the Bank Customer Churn Prediction project.

    Parameters:
        tab_name (streamlit.DeltaGenerator): Streamlit tab to display the content.
    """
    # Header and link to the dataset on Kaggle
    tab_name.subheader("Bank Customer Churn Prediction based on the following dataset:")
    tab_name.markdown("[Bank Customer Dataset for Churn prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)")

    # Project details
    tab_name.markdown(
        """
        ### In this project:
        - An exploratory data analysis is done (both univariate and bivariate analysis).
        - GridSearchCV is used to train multiple classification algorithms, fine-tune them, and find the best algorithm for the project.
        - Gradient Boosting Classifier achieved the highest score on the test data (86.5%)
        - Streamlit is used for deployment.
        """
        , unsafe_allow_html=True)

    # Link to the GitHub repository
    tab_name.write("The link of the GitHub repository is the following:")
    tab_name.markdown("[GitHub Repo](https://github.com/AbdelrahmanSabriAly/Churn_Prediction.git)")
