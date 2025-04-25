import streamlit as st
import pandas as pd
from pages.util.db import Todo, create_db_connection

session, engine = create_db_connection()
query = session.query(Todo)

df = pd.read_sql(query.statement, engine)
df.columns=['','タイトル','内容','締切','実施']
df = df.set_index('')
df

