import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer 
import joblib 
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["job_data"]
collection=db["job_posting"]

data=list(collection.find())
df=pd.DataFrame(data)

x=df["description"]
y=df["fraudulent"].astype(int)

vectorizer=TfidfVectorizer()
x_vec=vectorizer.fit_transform(x)

model=LogisticRegression()
model.fit(x_vec,y)

joblib.dump(vectorizer,"veck.pkl")
joblib.dump(model,"model.pkl")


