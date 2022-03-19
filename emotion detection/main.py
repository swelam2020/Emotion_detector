from fastapi import FastAPI
import uvicorn
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

import pickle
from emotions import sent

app = FastAPI()
pickle_in = open('final_model.pkl', 'rb')
classifier = pickle.load(pickle_in)


@app.get("/")
async def root():
    return {"message": "Hello from the emotion  classifier API"}


@app.post("/predict")
def predict_lang(data: list[str]):
    r=[]
    pred = classifier.predict(data)
    for i in pred:
        if i == 0 :
            r.append('anger')
        elif i == 1:
            r.append('happiness')
        elif i == 2:
            r.append('neutral')
        elif i == 3 :
            r.append('sadness')

    return {'prediction': r}
