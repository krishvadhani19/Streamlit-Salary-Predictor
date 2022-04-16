import matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.figure_factory as ff


data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

# using in-built functions to plot 
st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

# using matplotlib for plotting matplotlib
plt.scatter(data['a'], data['b'])
plt.title('scatter')
plt.ylabel('A')
plt.xlabel('B')
st.pyplot()

# Using altair Chart
# to create interactive plots
chart = alt.Chart(data).mark_circle().encode(
    x='a', y='b', tooltip = ['a', 'b']
)

st.altair_chart(chart, use_container_width=True)

# create flow-charts in streamlit
st.graphviz_chart("""
digraph{
    watch -> like
    like-> share
    share -> subscribe
    share -> watch
}

""")

# using plotly
plot = ff.create_scatterplotmatrix(data)
st.plotly_chart(plot, use_container_width=True)

# if we wish to plot a map

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

st.map(city)

# to add photo to the streamlit 
st.image('data\ms.png')

# to add audio to streamlit 
# st.audio()

# to add video to streamlit
st.video('https://www.youtube.com/watch?v=VDwka__-ScA&ab_channel=Wecan')