#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data1=request.form['jobType']
    data2=request.form['degree']
    data3=request.form['major']
    data4=request.form['industry']
    data5=request.form['yearsExperience']
    data6=request.form['milesFromMetropolis']
    arr =np.array([[data1,data2,data3,data4,data5,data6]])
    pred=model.predict(arr)
    

    return render_template('index.html', prediction_text='Salary is {}'.format(pred))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)


# In[ ]:




