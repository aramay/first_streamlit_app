import streamlit as st
import pandas as pd
import requests as re
import snowflake.connector
from urllib.error import URLError

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

def get_fruitvice_data(this_fruit_choice):
  
  fruityvice_res = re.get('https://www.fruityvice.com/api/fruit/' + fruit_choice)
  #st.text(fruityvice_res.json())

  # take the json version on response and normalize it
  fruityvice_normalized = pd.json_normalize(fruityvice_res.json())
  return fruityvice_normalized
  # output it - as a table
  #st.dataframe(fruityvice_normalized)

  

try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error('Please select a fruit to get information')
  else:
    back_from_func = get_fruitvice_data(fruit_choice)
    st.dataframe(back_from_func)

    
    #st.write('The user entered', fruit_choice)
   # fruityvice_res = re.get('https://www.fruityvice.com/api/fruit/' + fruit_choice)
    #st.text(fruityvice_res.json())

    # take the json version on response and normalize it
    #fruityvice_normalized = pd.json_normalize(fruityvice_res.json())
    # output it - as a table
    #st.dataframe(fruityvice_normalized)
    
    
except URLError as e:
  st.error()




#stop adding fruitsst.stop() 
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur
  my_cur.execute("insert into fruit_load_list values ('from streamlit')")
  return 'Thanks for adding ' + new_fruit
  

#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
#st.text("Hello from Snowflake:")
st.text("Fruit load list contains")
st.dataframe(my_data_rows)


add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_func = insert_row_snowflake(add_my_fruit)
  st.text(back_from_func)
  


#st.write('Thanks for adding ', fruit_choice)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
