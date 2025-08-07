import pandas as pd
from pymongo import MongoClient

df=pd.read_csv("fake_job_postings.csv")

df.dropna(subset=["title","description","fraudulent"],inplace=True)

client=MongoClient("mongodb://localhost:27017/")

db=client["job_data"]
collection=db["job_posting"]

data=df.to_dict(orient='records')

collection.insert_many(data)

print("added")
