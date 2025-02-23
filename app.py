# app.py
from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('rf_classifier.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        data = request.get_json()
        # Get data from the form (blood content values)
        Age = float(data['Age'])
        Gender = float(data['Gender'])
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
 
# Required for Vercel
def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == "__main__":
    app.run(debug=True)
