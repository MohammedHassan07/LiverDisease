# Liver Disease Prediction using Flask

This is a Flask-based web application that predicts whether a person is affected by liver disease based on blood content values.

## Installation and Setup

Follow these steps to set up and run the project on Windows:

### 1. Clone the Repository
```sh
git https://github.com/MohammedHassan07/LiverDisease
cd LiverDisease
```
### 2. Create virtual environment
```sh 
python -m venv venv
```
### 3. Activate the Virtual Environment
```sh
venv\Scripts\activate
```

### 4. Install Dependencies  
```sh
pip install -r requirements.txt
```
### 5. Run the Flask App
```sh
python app.py
```

### 6. Access the Application
```sh
http://127.0.0.1:5000
```

## Sample JSON
```json
{
  "Age": 0.0,
  "Gender": 0.0,
  "Total_Bilirubin": 0.0,
  "Direct_Bilirubin": 0.0,
  "Alkaline_Phosphotase": 0.0,
  "Alamine_Aminotransferase": 0.0,
  "Aspartate_Aminotransferase": 0.0,
  "Total_Protiens": 0.0,
  "Albumin": 0.0,
  "Albumin_and_Globulin_Ratio": 0.0
}

```