
# Exemplo de conexão com PostgreSQL
import psycopg2

def connect_postgres(host, database, user, password, port=5432):
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    return conn

# Exemplo de conexão com Firebird
import fdb

def connect_firebird(host, database, user, password, port=3050):
    conn = fdb.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )
    return conn

# Exemplo de conexão com SQL Server
import pyodbc

def connect_sqlserver(server, database, user, password, driver="ODBC Driver 17 for SQL Server"):
    conn_str = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={user};"
        f"PWD={password}"
    )
    conn = pyodbc.connect(conn_str)
    return conn
