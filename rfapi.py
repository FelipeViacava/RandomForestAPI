from flask import Flask, jsonify, request
import pickle
import pandas as pd
import json

with open('model.pickle', 'rb') as f:
    clf = pickle.load(f)

app = Flask(__name__)
@app.route("/RandomForest", methods=['GET','POST'])
def predict():
    data = request.json

    data = data['data']

    df = pd.DataFrame()
    columns = list(data.keys())

    for col in columns:
        df[col] = [data[col]]
        print(col)
    
    #df['female'] = df['Sex'].apply(lambda sex: 1 if sex == 'female' else 0)
    
    #df['1Class'] = df['Pclass'].apply(lambda pclass: 1 if pclass==1 else 0)
    #df['2Class'] = df['Pclass'].apply(lambda pclass: 1 if pclass==2 else 0)
    #df = df.drop(['Sex','Pclass'],axis=1)

    #x = df.values
    #prediction = clf.predict(x)[0]

    #return jsonify({'prediction': prediction})

    return jsonify({'True':True})

if __name__ == '__main__':
    app.run(debug=True)