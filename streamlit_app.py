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

my_fruit_list = my_fruit_list.set_index('Fruit')

#Add an interactive widget called Multi-select
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


