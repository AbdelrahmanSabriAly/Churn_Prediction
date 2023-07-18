import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pickle


from utils.EDA import show_EDA
from utils.APP import show_APP
from utils.contact import show_contact
from utils.about import ABOUT


st.set_page_config(layout="wide",page_title="Bank Customer Churn Prediction",page_icon='🏦')

# CSS style to hide Streamlit's main menu and footer
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer{visibility: hidden;}
</style>
"""

# Applying the CSS style to hide Streamlit's main menu and footer
st.markdown(hide_st_style, unsafe_allow_html=True)



# Load the model from the file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


df = pd.read_csv("Churn_data.csv")
df = df.drop(['RowNumber','CustomerId','Surname'],axis = 1)
# List the columns that need label encoding
categorical_cols = df.select_dtypes(include = "object").columns

# List the numerical columns that need standard normalization
numerical_cols = df.select_dtypes(exclude = "object").columns


def header(url):
     st.markdown(f'<p style="background-color:#17123B;color:#55C9F2;font-size:42px;border-radius:2%;font-weight:bold;">{url}</p>', unsafe_allow_html=True)
header("Bank Customer Churn Prediction 🏦")
about,eda,app,contact = st.tabs(['About','Exploratory Data Analysis','App','Contact'])

# ===================================== {About} ================================================

ABOUT(about)

# ====================================== {EDA} =================================================

show_EDA(eda,df,categorical_cols,numerical_cols)

# ====================================== {App} =================================================

show_APP(app,df,categorical_cols,model)

# ==================================== {Contact} ===============================================

show_contact(contact)
