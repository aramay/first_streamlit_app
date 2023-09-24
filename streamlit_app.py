import streamlit as st
import pandas as pd
import requests as re
import snowflake.connector

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

# Fruityvice Fruit Advice
st.header('Fruityvice Fruit Advice')

fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)

fruityvice_res = re.get('https://www.fruityvice.com/api/fruit/' + fruit_choice)

#st.text(fruityvice_res.json())

# take the json version on response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_res.json())
# output it - as a table
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
