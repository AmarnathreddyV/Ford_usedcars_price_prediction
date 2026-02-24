# Ford_usedcars_price_prediction

# 🚗 Car Price Prediction App

This project is a Machine Learning based web application that predicts the selling price of used Ford cars based on user inputs such as year, mileage, engine size, fuel type, transmission, and model.

The application is built using Streamlit and a RandomForest Regression model trained on a UK used-car dataset.

---

## 📌 Project Overview

- Type: Supervised Machine Learning (Regression)
- Algorithm: Random Forest Regressor
- Frontend: Streamlit
- Backend: Python, scikit-learn
- Dataset: Ford Used Car Dataset (UK market)
- Output: Predicted Car Price (in GBP)

---

## ⚙️ Features

- Predicts used car prices instantly
- User-friendly Streamlit interface
- Supports multiple car models
- Uses One-Hot Encoding for categorical variables
- Displays realistic resale prices
- Easy deployment on Streamlit Cloud

---

## 🧠 Machine Learning Workflow

1. Load dataset (ford.csv)
2. Preprocess data (handle categorical features using one-hot encoding)
3. Split dataset into training and testing sets
4. Train RandomForestRegressor model
5. Save trained model using joblib
6. Build Streamlit UI (app.py)
7. Load model and predict price based on user input

---

## 📁 Project Structure

car_price_prediction/
│
├── app.py
├── ford.csv
├── model.pkl
├── requirements.txt
└── README.md



---

## ▶️ How to Run Locally

1. Clone the repository:
git clone https://github.com/your-username/car-price-prediction.git


2. Navigate to project folder:
cd car-price-prediction



3. Install dependencies:
pip install -r requirements.txt



4. Run Streamlit app:
streamlit run app.py





---

## 📦 Requirements

- streamlit  
- pandas  
- numpy  
- scikit-learn  
- joblib  

(All listed in requirements.txt)

---

## 🎯 Model Inputs

- Year
- Mileage
- Engine Size
- Fuel Type
- Transmission
- Model

---

## 📤 Output

- Predicted Used Car Price (GBP)

---

## 🚀 Deployment

This app can be deployed on Streamlit Community Cloud by connecting this GitHub repository.

---

## 📚 Learning Outcomes

- Hands-on experience with regression models
- Feature engineering using One-Hot Encoding
- Model deployment using Streamlit
- End-to-end ML project development

---

## 👨‍💻 Author

Amarnath Reddy  
B.Tech CSE (AIML)
Aspiring Data Scientist

---

## ⭐ Acknowledgement

Dataset inspired by UK Ford used car listings.

---

Thank you for checking out this project!
