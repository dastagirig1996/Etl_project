import boto3
import sys
path = r"C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\config"
sys.path.append(path)
from config.aws_credentials import Access_key_ID, Secret_access_key
s3 = boto3.client("s3",aws_access_key_id = Access_key_ID, aws_secret_access_key = Secret_access_key )
s3.upload_file("C:\PROFFESSION\Data_Engneer_Projects\Finance_EtL_Project\data\customers_by_year.csv","aja-bucket", "customers_data_by_year.csv")