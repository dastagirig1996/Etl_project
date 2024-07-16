import mysql.connector ## does not support for pandas
import pandas as pd
from sqlalchemy import create_engine

def extract_data():
    query = "select * from customers"
    connection = create_engine("mysql+pymysql://root:root@localhost/finance_data")
    df = pd.read_sql_query(query, connection)
    df.to_csv("C:/PROFFESSION/Data_Engneer_Projects/Finance_EtL_Project/data/customers_db.csv", index = False)

# C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\data