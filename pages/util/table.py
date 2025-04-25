import pandas as pd
from pages.util.db import Todo

def create_dataframe(session, engine):
    query = session.query(Todo)
    df = pd.read_sql(query.statement, engine)
    df.columns=['','タイトル','内容','締切','実施']
    return df.set_index('')

