from operator import index
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Widgets')

# to add button
if st.button('Subscribe'):
    st.write('Like this video too')

# to add a text input
name = st.text_input('Name')
st.write(name)

# to add a text area
address = st.text_area('Enter your address')
st.write(address)

# to add a date input
st.date_input('enter a date')

# to add a time input
st.time_input('enter a time input')

# to add a checkbox
if st.checkbox("You accept the T&C ", value=False):
    st.write('Thank You!')

# to add radio button
v1 = st.radio('Colours',['r','g','b'], index=1)

# to add select box
v2 = st.selectbox('Colours', ['r','g','b'], index=1)

st.write(v1, v2)

# to add multi-selectbox
v3 = st.multiselect('Colours', ['r', 'g', 'b'])
st.write(v3)

# to add slider
st.slider('age', min_value=18, max_value=89, step=2)

# to add number input
st.number_input('Numbers', min_value=1.0, max_value=10.0, value = 7.0,step=1.0)

# to add a file uploader
img = st.file_uploader('Upload a File')
if img:
    st.image(img)