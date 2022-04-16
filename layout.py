import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Registration Form')

# having two inputs in the same line

# First Name and Last Name
first, last = st.columns(2)
first.text_input('First Name:')
last.text_input('Last Name:')

# Email and Number
email, mob = st.columns([3,1])
email.text_input('Email:')
mob.text_input('Mobile Number:')

# user and passwaord
user, pw, pw2 = st.columns([2,1,1])
user.text_input('Username:')
pw.text_input('Create Password:', type='password')
pw2.text_input('Re-enter Password', type='password')

# checkbox, and submit
ch, bl, sub = st.columns(3)
ch.checkbox('I agree:')
sub.button('Submit')