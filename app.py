import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pickle

# Importing custom utility functions
from utils.EDA import show_eda
from utils.APP import show_app
from utils.contact import show_contact
from utils.about import display_about_info

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Bank Customer Churn Prediction", page_icon='🏦')

# CSS style to hide Streamlit's main menu and footer
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# Applying the CSS style to hide Streamlit's main menu and footer
st.markdown(hide_st_style, unsafe_allow_html=True)

# Load the trained model from the file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Read the dataset and preprocess it
df = pd.read_csv("Churn_data.csv")
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# List the columns that need label encoding
categorical_cols = df.select_dtypes(include="object").columns

# List the numerical columns that need standard normalization
numerical_cols = df.select_dtypes(exclude="object").columns

# Function to display header with custom styling
def header(url):
    st.markdown(f'<p style="background-color:#17123B;color:#55C9F2;font-size:42px;border-radius:2%;font-weight:bold;">{url}</p>', unsafe_allow_html=True)

# Display header for the app
header("Bank Customer Churn Prediction 🏦")

# Create tabs for different sections of the app
about_tab, eda_tab, app_tab, contact_tab = st.tabs(['About', 'Exploratory Data Analysis', 'App', 'Contact'])

# ===================================== {About} ================================================

# Display information about the project in the "About" tab
display_about_info(about_tab)

# ====================================== {EDA} =================================================

# Perform Exploratory Data Analysis in the "Exploratory Data Analysis" tab
show_eda(eda_tab, df, categorical_cols, numerical_cols)

# ====================================== {App} =================================================

# Run the prediction app in the "App" tab
show_app(app_tab, df, categorical_cols, model)

# ==================================== {Contact} ===============================================

# Display contact information in the "Contact" tab
show_contact(contact_tab)
