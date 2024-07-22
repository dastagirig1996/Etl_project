import pandas as pd
import boto3
import sys
sys.path.append("Finance_EtL_Project")
from config.aws_credentials import get_secrets
import sys

def load_data():
    df = pd.read_csv("Finance_EtL_Project/data/customers_by_year.csv")
    assert df["registration_date"].min()>=2000  #" It is established in 2000"
    # path = r"Finance_EtL_Project/config"
    # sys.path.append(path)
    secrets = get_secrets()
    s3 = boto3.client("s3",aws_access_key_id = secrets["aws_access_key_id"], aws_secret_access_key = secrets["aws_secret_access_key"] )
    s3.upload_file("Finance_EtL_Project\data\customers_by_year.csv","etl-finance-data-bucket", "customers_data_by_year.csv")
    print("loading done")

# load_data()
