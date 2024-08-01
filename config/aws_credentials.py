import boto3
import json
import os
def get_mysql_secrets():
    session = boto3.session.Session()
    client = session.client(
        service_name = 'secretsmanager',
        region_name = os.getenv("aws_cred_region")

    )
    try:
        get_secret_value_response = client.get_secret_value(SecretId = os.getenv("aws_rds_secrets"))

    except Exception as e:
        print(f"Error getting on secret:{e}")
        return None
    
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)
  #  creds = json.loads(secret)
 #   print(creds)
#get_mysql_secrets()

def get_secrets():
    cred_secret = os.getenv("aws_cred_secret")
    secret_name =cred_secret
    session = boto3.session.Session()
    client = session.client(service_name = "secretsmanager",region_name = os.getenv("aws_cred_region"))
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise e
    
    # Decrypts secret using the associated KMS key
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)
    # creds = json.loads(secret)
#     print(creds)
# get_secrets()
    

