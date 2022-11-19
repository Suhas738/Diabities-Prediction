from django.shortcuts import render
import pickle
import numpy as np

def home(req):
    model = pickle.load(open('pima-trained-model.sav','rb'))
  
    data = np.array([1,103,30,38,83,43.3,0.183,33]).reshape(1,-1)
    result = model.predict(data)
    return render(req,"index.html",{"testing":result})