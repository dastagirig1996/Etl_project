# import mysql.connector ## does not support for pandas
import pandas as pd
from sqlalchemy import create_engine
import sys
sys.path.append("Finance_EtL_Project")

from config.aws_credentials import get_mysql_secrets

def extract_data():
    query = "select * from customers"
    # connection = create_engine("mysql+pymysql://root:root@localhost/finance_data")
    secret = get_mysql_secrets()
    user = secret["username"]
    password = secret["password"]
    host = secret['host']
    db_name = secret["dbname"]
    connection = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_name}")
    print("connection done")
    df = pd.read_sql_query(query, connection)
    df.to_csv("Finance_EtL_Project/data/customers_db.csv", index = False)
    print("extraction done")
# extract_data()
# C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\data