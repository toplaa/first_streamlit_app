import streamlit 

streamlit.title('My Parent New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text ('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiled Free Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)

#Add an interactive widget called Multi-select
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
