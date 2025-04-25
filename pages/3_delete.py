import streamlit as st
import pandas as pd
from pages.util.db import create_db_connection, Todo
from pages.util.table import create_dataframe

# DB settings
session, engine = create_db_connection()
df = create_dataframe(session, engine)
df['削除'] = False

df = st.data_editor(df)

def delete():
    for row in df[df['削除'] == True].iterrows():
        todo = session.get(Todo, row[0]) # row[0]でindexを取得
        session.delete(todo)
        session.commit()

clicked = st.button('削除', type='primary', on_click=delete)

if (clicked): st.switch_page('index.py')

