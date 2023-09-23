import streamlit as st
import pandas as pd

st.title("My parents kitchen")

st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# add pick list here
st.multiselect("Pick some fruits ", list(fruits_list))

# display the table
st.dataframe(fruits_list)
