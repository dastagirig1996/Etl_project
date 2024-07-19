import pandas as pd
import boto3
import sys

def load_data():
    df = pd.read_csv("C:/PROFFESSION/Data_Engneer_Projects/Finance_EtL_Project/data/customers_by_year.csv")
    assert df["registration_date"].min()>=2000  #" It is established in 2000"
    path = r"C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\config"
    sys.path.append(path)
    from config.aws_credentials import Access_key_ID, Secret_access_key
    s3 = boto3.client("s3",aws_access_key_id = Access_key_ID, aws_secret_access_key = Secret_access_key )
    s3.upload_file("C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\data\customers_by_year.csv","aja-bucket", "customers_data_by_year.csv")
# import os

# print(os.getenv("hello"))
# print(os.getenv("adeed "))
# # os.environ["adeed"]="123654"