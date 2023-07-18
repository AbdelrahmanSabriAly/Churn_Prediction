import streamlit as st
import pandas as pd
import numpy as np 
import plotly.graph_objects as go
import matplotlib.pyplot as plt


colors = ['#F94332','#54CF53','#55C9F2','#ECE72C','#2A2953']
#plot_bgcolor='#2A2953'

def show_EDA(tab_name,df,categorical_cols,numerical_cols):
    tab_name.title("Exploratory Data Analysis")
    tab_name.subheader("Univariate Analysis")
    tab_name.subheader("1- Categorical columns:")
    for col in categorical_cols:
    
        # Sample data for the pie chart
        labels = df[col].value_counts().index
        values = df[col].value_counts()

        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=colors))])

        # Add a title to the chart
        fig.update_layout(title=col)



        # Show the chart
        tab_name.plotly_chart(fig)


    tab_name.markdown(
    """
    ### Insights from categorical columns:
    - Most customers are from France
    - Number of male customers are greater than the number of female customers
    """
    ,unsafe_allow_html=True)
    tab_name.markdown("""---""")

    tab_name.subheader("2- Numerical columns:")

    for col in numerical_cols:
        if df[col].nunique() >11:

            # Sample data for the histogram
            data = df[col]

            # Create the histogram
            fig = go.Figure(data=[go.Histogram(x=data,marker_color='#55C9F2')])

            # Add a title to the chart
            fig.update_layout(title=col)

            # Show the chart
            tab_name.plotly_chart(fig)
            
        else: 

            # Sample data for the pie chart
            labels = df[col].value_counts().index
            values = df[col].value_counts()

            # Create the pie chart
            fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=colors))])

            # Add a title to the chart
            fig.update_layout(title=col)

            # Show the chart
            tab_name.plotly_chart(fig)

    tab_name.markdown(
    """
    ### Insights from numeric columns:
    - Most credit scores are between 600 and 700
    - Most common ages are between 30 and 40
    - There are 11 balanced tenures
    - Most frequent balances are between 0 and 2500 USD
    - Most customers tend to buy 1 or 2 products
    - Most customers have Credit Card
    - Number of active customers is nearly equal to the number of inaictive customers
    - There are varity of estimated salaries in the dataset
    - The target columns "Esited" has an unbalanced 2 classes. Thus, Ensemble algorithms will be used for prediction
    """
    ,unsafe_allow_html=True)


    tab_name.markdown("""---""")
    tab_name.markdown("""---""")

    tab_name.subheader("Bivariate Analysis")
    tab_name.subheader("1- Categorical columns:")
    for col in categorical_cols:
        # Sample data for the pie chart
        labels = df.groupby(col).mean()['Exited'].index
        values = df.groupby(col).mean()['Exited']

        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=colors))])

        # Add a title to the chart
        title = f"Effect of {col} on Excitement"
        fig.update_layout(title=title)

        # Show the chart
        tab_name.plotly_chart(fig)

    tab_name.markdown(
    """
    ### Insights from categorical columns:
    - France has the largest number of exited customers
    - Most exited customers are males 
    """
    ,unsafe_allow_html=True)
    tab_name.markdown("""---""")
    tab_name.subheader("2- Numerical columns:")


    for col in numerical_cols[:-1]:
        if df[col].nunique()>11:
            # Assuming you have two arrays x and y representing your data points
            x = df.groupby(col).count().index
            y = df.groupby(col).count()['Exited']

        # Create a line plot
            line_plot = go.Scatter(x=x, y=y, mode='lines', name='Line Plot',line=dict(color='#55C9F2'))

            # Create the layout for the plot
            layout = go.Layout(
                title=f"Effect of {col} on Excitement",
                xaxis=dict(title=col),
                yaxis=dict(title="Number of exited people"),

            )

            # Create the figure and add the line trace
            fig = go.Figure(data=[line_plot], layout=layout)

            # Show the plot
            tab_name.plotly_chart(fig)
            
        else: 

            # Sample data for the pie chart
            labels = df.groupby(col).count().index
            values = df.groupby(col).count()['Exited']

            # Create the pie chart
            fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=colors))])

            # Add a title to the chart
            fig.update_layout(title=col)

            # Show the chart
            tab_name.plotly_chart(fig)

    tab_name.markdown(
    """
    ### Insights from numeric columns:
    - Most exited customers have a credit score between 600 and 700
    - Most exited customers are (30 - 40) years old
    - Tenures between 1 and 9 have the largest number of exited customers
    - All exited customers have 0 balance
    - Most exited customers has purchased 1 or 2 products
    - Most exited customers has Credit Card
    - Exitement does not depend on inactivity or salary
    """
    ,unsafe_allow_html=True)








        



