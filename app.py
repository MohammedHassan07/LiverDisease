from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
from tensorflow import keras

app = Flask(__name__)

model = joblib.load('rf_classifier.pkl')
model2 = keras.models.load_model('liver_disease_l1l2_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        data = request.get_json()
        # Get data from the form (blood content values)
        # Age = float(data['Age'])
        # Gender = float(data['Gender'])
        Total_Bilirubin = float(data['Total_Bilirubin'])
        Direct_Bilirubin = float(data['Direct_Bilirubin'])
        Alkaline_Phosphotase = float(data['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = float(data['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = float(data['Aspartate_Aminotransferase'])
        Total_Protiens = float(data['Total_Protiens'])
        Albumin = float(data['Albumin'])
        Albumin_and_Globulin_Ratio = float(data['Albumin_and_Globulin_Ratio'])

        # Prepare the input for prediction
        input_data = np.array([[Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, 
                                Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, 
                                Albumin, Albumin_and_Globulin_Ratio]])

        # Predict the disease (1: Disease, 0: No Disease)
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "Disease Detected"
         
        else:
            result = "No Disease Detected"
            
        print('result -->', result)
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'prediction': f"Error: {str(e)}"})
 
@app.route('/predict2', methods=['POST'])
def predict2():
    data = request.get_json() 
    print(data)

    features = [
        float(data['Total_Bilirubin']), float(data['Direct_Bilirubin']),
        float(data['Alkaline_Phosphotase']),
        float(data['Alamine_Aminotransferase']),
        float(data['Aspartate_Aminotransferase']),
        float(data['Total_Protiens']),
        float(data['Albumin']),
        float(data['Albumin_and_Globulin_Ratio'])
    ]

    input_data = np.array(features).reshape(1, -1)  
    
    prediction = model2.predict(input_data)[0][0] 
    
    return jsonify({'prediction': prediction}) 

if __name__ == "__main__":
    app.run(debug=True)
