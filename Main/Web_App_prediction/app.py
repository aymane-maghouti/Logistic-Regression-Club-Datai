import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle
from data_encoding import encode_Data
from sklearn.linear_model import LogisticRegression



app = Flask(__name__)

model = pickle.load(open('models/classifier.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        data = request.json


        res = model.predict([encode_Data(data)])

        if res == 1:
            res = 'Yes'
        elif res == 0:
            res = 'No'

        print(res)
        return jsonify({'estimation': res})

if __name__ == '__main__':
    app.run(debug=True)
