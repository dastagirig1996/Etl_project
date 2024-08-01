# import mysql.connector ## does not support for pandas
import pandas as pd
from sqlalchemy import create_engine
import sys
import os 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
config_path = os.path.join(project_root, 'config')
sys.path.append(config_path)

# Diagnostics
print("Current Working Directory:", os.getcwd())
print("sys.path:", sys.path)

try:
    from aws_credentials import get_mysql_secrets
    print("Import successful")
except ModuleNotFoundError as e:
    print("Import failed:", e)

def extract_data():
    query = "select * from customers"
    # connection = create_engine("mysql+pymysql://root:root@localhost/finance_data")
    secret = get_mysql_secrets()
    user = secret["username"]
    password = secret["password"]
    host = secret['host']
    db_name = secret["dbname"]
    connection_string=f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
    connection = create_engine(connection_string)
    print("connection done")
    df = pd.read_sql_query(query, connection)
    df.to_csv("/home/ubuntu/Etl_project/data/customers_db.csv", index = False)
    print("extraction done")
#extract_data()
# C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\data
