import pandas as pd

def transform_data():
    file_path = "Finance_EtL_Project\data\customers_db.csv"
    df = pd.read_csv(file_path)
    df["registration_date"] = df["registration_date"].apply(lambda x: x.split("-")[0])
    df["registration_date"] = df["registration_date"].astype(int)
    customers_by_year = df.groupby("registration_date").size().reset_index(name = 'count')
    customers_by_year.to_csv("Finance_EtL_Project/data/customers_by_year.csv",index = False)
    print("trnasform done")
# transform_data()