import pickle
import numpy as np

from flask import Flask
from flask import request
from flask import jsonify

input_file = "best_model_capst.pkl"
input_file2 = "dicv.pkl"

with open(input_file, 'rb') as f_in: 
    model = pickle.load(f_in)
    
with open(input_file2, 'rb') as f_in2: 
    dv = pickle.load(f_in2)
    
app = Flask('staff_Attrition')

@app.route('/predict', methods = ['POST'])
def predict():
    staff = request.get_json()
    
    X = dv.transform([staff])
    staff_attrition = model.predict_proba(X)[:, 1]
    if staff_attrition < 0.5:
        attri = "Staff less likely leave organisation"
    else:
        attri = "Staff likely to leave organisation"
    
    result = {
        'Probability_Attrition: ': float(staff_attrition),
        'Attrition_Status': attri
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 6090)