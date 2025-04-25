import streamlit as st
from pages.util.db import create_db_connection, Todo
from pages.util.table import create_dataframe

# DB settings
session, engine = create_db_connection()
df = create_dataframe(session, engine)
df_orig = df.copy()

df = st.data_editor(df)

def update_table():
    updates = []
    for i in range(len(df)):
        if not df.iloc[i].equals(df_orig.iloc[i]):
            d = dict(df.iloc[i]); d['id'] = df.index[i]
            updates.append(d)
    for row in updates:
        todo = session.get(Todo, int(row['id']))
        todo.title = row['タイトル']; todo.content = row['内容']
        todo.deadline = row['締切']; todo.done = row['実施']
    session.commit()    

clicked = st.button('保存', type='primary', on_click=update_table)

if (clicked): st.switch_page('index.py')

