import streamlit

streamlit.title(' my parent new healty diner')
streamlit.header('  breakfast menu')
streamlit.text(' 🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kali , spinach & Rocket Smoothie')
streamlit.text('🐔 OHard-Boiled Free range Egg')
streamlit.text('🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))



