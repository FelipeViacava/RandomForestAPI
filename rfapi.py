from flask import Flask, jsonify, request
import pickle
import pandas as pd
import json

with open('model.pickle', 'rb') as f:
    clf = pickle.load(f)

app = Flask(__name__)
@app.route("/RandomForest", methods=['GET','POST'])
def predict():
    payload = request.json
    data = payload['data']

    df = pd.DataFrame()
    columns = list(data.keys())
    for col in columns:
        df[col] = [data[col]]
    
    df['female'] = df['Sex'].apply(lambda sex: 1 if sex == 'female' else 0)
    df['1Class'] = df['Pclass'].apply(lambda pclass: 1 if pclass==1 else 0)
    df['2Class'] = df['Pclass'].apply(lambda pclass: 1 if pclass==2 else 0)
    df = df.drop(['Sex','Pclass'],axis=1)

    x = df.values
    y = clf.predict(x)[0]

    if y == 1:
        prediction = 'According to our model, you would survive the Titanic disaster!'
    else:
        prediction = 'According to our model, you would not survive the Titanic disaster.'

    return jsonify({'Prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)