import streamlit as st
import pandas as pd
from pages.util.db import create_db_connection, Todo

# DB settings
session, engine = create_db_connection()

# User interface
title = st.text_input(label='タイトル')
memo = st.text_area(label='内容')
date = st.date_input(label='締切')
done = False

def append():
    df = pd.DataFrame({'title': [title], 'content': [memo], 
                       'deadline': [date], 'done': [done]})
    df.to_sql('todo', engine, if_exists='append', index=False)

clicked = st.button('登録', type='primary', on_click=append)

if (clicked): st.switch_page('index.py')

