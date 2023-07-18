import streamlit as st
import pandas as pd
import plotly.graph_objects as go

colors = ['#F94332', '#54CF53', '#55C9F2', '#ECE72C', '#2A2953']

def show_eda(tab_name, df, categorical_cols, numerical_cols):
    """
    Displays the Exploratory Data Analysis (EDA) for the given dataset.

    Parameters:
        tab_name (streamlit.DeltaGenerator): Streamlit tab to display the content.
        df (pandas.DataFrame): DataFrame containing the dataset with the target column "Exited".
        categorical_cols (list): List of categorical columns in the dataset.
        numerical_cols (list): List of numerical columns in the dataset.
    """
    # Univariate Analysis - Categorical Columns
    tab_name.title("Exploratory Data Analysis")
    tab_name.subheader("Univariate Analysis")
    tab_name.subheader("1- Categorical Columns:")
    for col in categorical_cols:
        # Sample data for the pie chart
        labels = df[col].value_counts().index
        values = df[col].value_counts()

        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

        # Add a title to the chart
        fig.update_layout(title=col)

        # Show the chart
        tab_name.plotly_chart(fig)

    # Insights from categorical columns
    tab_name.markdown(
        """
        ### Insights from Categorical Columns:
        - The majority of customers are from France.
        - The number of male customers is greater than the number of female customers.
        """
        , unsafe_allow_html=True)
    tab_name.markdown("""---""")

    tab_name.subheader("2- Numerical Columns:")
    for col in numerical_cols:
        if df[col].nunique() > 11:
            # Sample data for the histogram
            data = df[col]

            # Create the histogram
            fig = go.Figure(data=[go.Histogram(x=data, marker_color='#55C9F2')])

            # Add a title to the chart
            fig.update_layout(title=col)

            # Show the chart
            tab_name.plotly_chart(fig)
        else:
            # Sample data for the pie chart
            labels = df[col].value_counts().index
            values = df[col].value_counts()

            # Create the pie chart
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

            # Add a title to the chart
            fig.update_layout(title=col)

            # Show the chart
            tab_name.plotly_chart(fig)

    # Insights from numeric columns
    tab_name.markdown(
        """
        ### Insights from Numerical Columns:
        - The majority of credit scores are between 600 and 700.
        - The most common ages of customers are between 30 and 40.
        - There are 11 distinct tenures with balanced distribution.
        - Most customers have account balances between 0 and 2500 USD.
        - The majority of customers tend to buy 1 or 2 products.
        - Most customers have a Credit Card.
        - The number of active customers is nearly equal to the number of inactive customers.
        - The dataset contains a variety of estimated salaries.
        - The target column "Exited" exhibits an unbalanced distribution with two classes. Therefore, Ensemble algorithms will be used for prediction.
        """
        , unsafe_allow_html=True)

    tab_name.markdown("""---""")
    tab_name.markdown("""---""")

    # Bivariate Analysis - Categorical Columns
    tab_name.subheader("Bivariate Analysis")
    tab_name.subheader("1- Categorical Columns:")
    for col in categorical_cols:
        # Sample data for the pie chart
        labels = df.groupby(col).mean()['Exited'].index
        values = df.groupby(col).mean()['Exited']

        # Create the pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

        # Add a title to the chart
        title = f"Effect of {col} on Churn"
        fig.update_layout(title=title)

        # Show the chart
        tab_name.plotly_chart(fig)

    # Insights from categorical columns
    tab_name.markdown(
        """
        ### Insights from Categorical Columns:
        - Germany has the largest number of customers who have exited.
        - The majority of exited customers are females.
        """
        , unsafe_allow_html=True)
    tab_name.markdown("""---""")
    tab_name.subheader("2- Numerical Columns:")

    for col in numerical_cols[:-1]:
        if df[col].nunique() > 11:
            # Sample data for the line plot
            x = df.groupby(col).count().index
            y = df.groupby(col).count()['Exited']

            # Create a line plot
            line_plot = go.Scatter(x=x, y=y, mode='lines', name='Line Plot', line=dict(color='#55C9F2'))

            # Create the layout for the plot
            layout = go.Layout(
                title=f"Effect of {col} on Churn",
                xaxis=dict(title=col),
                yaxis=dict(title="Number of Exited Customers"),
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
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors))])

            # Add a title to the chart
            fig.update_layout(title=col)

            # Show the chart
            tab_name.plotly_chart(fig)

    # Insights from numeric columns
    tab_name.markdown(
        """
        ### Insights from Numerical Columns:
        - Most exited customers have a credit score between 600 and 700.
        - The majority of exited customers are between 30 and 40 years old.
        - Tenures between 1 and 9 have the largest number of exited customers.
        - All exited customers have a balance of 0.
        - Most exited customers have purchased 1 or 2 products.
        - Most exited customers have a Credit Card.
        - Exited status does not depend on inactivity or salary.
        """
        , unsafe_allow_html=True)
