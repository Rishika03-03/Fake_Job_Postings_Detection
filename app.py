from flask import Flask,request,redirect,render_template
import joblib
from pymongo import MongoClient

app=Flask(__name__)

vectorizer=joblib.load('veck.pkl')
model=joblib.load("model.pkl")

client=MongoClient("mongodb://localhost:27017/")
db=client['job_data']
collection=db["pred"]

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
  if request.method=="POST":
    des=request.form["description"]
    bec=vectorizer.transform([des])
    pred=model.predict(bec)
    result="fraudulent" if pred[0]==1 else "legit"

    collection.insert_one({"description":des,"prediction":result})
  return render_template("index.html",prediction=result)

if __name__=="__main__":
  app.run(port=9000,debug=True)