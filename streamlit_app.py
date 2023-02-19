import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError
streamlit.title(' my parent new healty diner')
streamlit.header('  breakfast menu')
streamlit.text(' 🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kali , spinach & Rocket Smoothie')
streamlit.text('🐔 OHard-Boiled Free range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))



def get_fruityvice_dat(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!") 
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error('please select a fruit to get informations')
  else :
   back_from_function=get_fruityvice_dat(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error
  


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains")

def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("SELECT * from fruit_load_list")
     return  my_cur.fetchall()
if streamlit.button('get fruit load list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows=get_fruit_load_list()
     streamlit.dataframe(my_data_rows)
def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into fruit_load_list values ('from streamlit')")
     return 'thanks for adding'+new_fruit
add_my_fruit=streamlit.text_input('What fruit would you like to add')
if streamlit.button('insert a fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function=insert_row_snowflake(new_fruit)
     streamlit.text('back from function)



