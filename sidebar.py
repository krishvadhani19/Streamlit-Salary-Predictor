import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

st.title('SideBar')
plt.style.use('ggplot')

data = {
    'num':[x for x in range(1,11)],
    'square':[x**2 for x in range(1,11)],
    'twice':[x*2 for x in range(1,11)],
    'thrice':[x*3 for x in range(1,11)]
}

df = pd.DataFrame(data)

# Sidebar Radio
rad = st.sidebar.radio('Navigation', ['Home', 'About US'])

if rad == 'Home':

    # Progress Bar
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress.progress(i+1)

    st.balloons()

    # Sidebar SelectBox
    col = st.sidebar.multiselect('Select a Column', df.columns)

    plt.plot(df['num'], df[col])

    st.pyplot()
else:
    # st.write('You are here in About US page')

    # Add status messages to streamlit application
    st.error('Error')
    st.success('Success')
    st.info('Information')
    st.exception(RuntimeError('This is an Error'))
    st.warning('This is a warning')
