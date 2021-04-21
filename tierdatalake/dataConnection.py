import pandas as pd
import cx_Oracle
from sqlalchemy import types, create_engine
import time

cx_Oracle.init_oracle_client(lib_dir = r"C:\Program Files\Python36\instantclient_19_6")
engine = create_engine('oracle://USUARIO:PASSWORD@IP:1521/dgpp', echo=False)

def qDataLakeConn(query):
    db_tables = pd.read_sql_query(query,engine)
    return db_tables
