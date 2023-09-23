import streamlit as st
import pandas as pd

st.title("My parents kitchen")

st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# pick fruits by name
fruits_list = fruits_list.set_index('Fruit')


# add pick list here
fruits_selected = st.multiselect("Pick some fruits ", list(fruits_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = fruits_list.loc[fruits_selected]
# display the table
st.dataframe(fruits_to_show)
