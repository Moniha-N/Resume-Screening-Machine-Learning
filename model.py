import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


df = pd.read_csv("resume_data.csv")


X = df[["experience", "projects", "certificates"]]
y = df["shortlisted"]


model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Logistic Regression model trained successfully")