import pyodbc

SERVER = "localhost"
DATABASE = "epsi_wis_db"
DRIVER = "{ODBC Driver 17 for SQL Server}"

conn_str = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};trusted_connection=yes"
conn = pyodbc.connect(conn_str)
print("Connexion réussie !")
conn.close()