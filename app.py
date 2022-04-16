from statistics import mode
from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.title('Salary Predictor')

# importing data
data = pd.read_csv('data\Salary_Data.csv')

# Linear Regression
model = LinearRegression()
x = data[['YearsExperience']]
y = data['Salary']
model.fit(x,y)

# SideBar
nav = st.sidebar.radio('Navigation',['Home', 'Prediction', 'Contribute'])

# Home
if nav == 'Home':
    # st.write('Home')

    # Image
    st.image('data\money.jpg', width=600)

    # Checkbox to display table
    if st.checkbox('Show Table'):
        st.table(data)

    # slider for changing the number of years
    val = st.slider('Filter data using years',min_value=0, max_value=20)

    # changing the data to reflect the changes onto the graph
    data = data[data['YearsExperience']>=val]

    # Selectbox for an interactive or non-interactive graph
    graph = st.selectbox('What kind of Graph?', ['Non-Interactive', 'Interactive'])

    # Interactive
    if graph == 'Interactive':
        fig = go.Figure(data=go.Scatter(x=data['YearsExperience'], y=data['Salary'], mode='markers'))
        st.plotly_chart(fig)
    # Non-Interactive
    if graph == 'Non-Interactive':
        plt.figure(figsize=(10,5))
        plt.scatter(data['YearsExperience'], data['Salary'])
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.tight_layout()
        st.pyplot()

# Prediction
if nav == 'Prediction':
    st.header('Know your Salary')
    val = st.number_input('Enter your exp', 0.0,20.0,step=0.25)
    val = model.predict(np.array(val).reshape(1,-1))

    if st.button('Predict'):
        st.success(f'Your predicted salary is: ${val[0]:.2f}')

# Contribute
if nav == 'Contribute':
    st.header('Contribute to our dataset')
    ex = st.number_input('Enter your experience',0,20)
    sal = st.number_input('Enter your Salary',0.00,1000000000.00, step=1000.00)
    if st.button('Submit'):
        extra_data = pd.DataFrame({'YearsExperience':[ex],'Salary':[sal]})
        extra_data.to_csv('data//Salary_Data.csv',mode='a',header=False, index=False)
        st.success('Submitted')
