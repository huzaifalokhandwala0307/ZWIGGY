# 🚚 Delivery Time Prediction ML Web App

A Machine Learning web application that predicts **food delivery time**, **restaurant preparation time**, and **possible delay reasons** using order details such as city, distance, traffic, weather, and peak hour conditions.

This project is built using **Python, Flask, and Scikit-Learn** and provides a simple web interface where users can enter order information and get delivery predictions.

---

# 📌 Features

✔ Predict delivery time  
✔ Predict restaurant preparation time  
✔ Identify possible delay reasons  
✔ Machine learning pipeline using Scikit-Learn  
✔ Web interface using HTML & CSS  
✔ Synthetic dataset generation for training  
✔ Model evaluation with regression and classification metrics  

---

# 🧠 Machine Learning Models

This project uses **three machine learning models**.

## 1️⃣ Preparation Time Model
Predicts how long a restaurant will take to prepare the order.

**Input**
- Restaurant name

**Model Used**
- Linear Regression

---

## 2️⃣ Delivery Time Model
Predicts the estimated delivery time using multiple factors.

**Inputs**
- City
- Distance (km)
- Number of items
- Peak hour
- Traffic level
- Weather
- Restaurant
- Preparation time

**Model Used**
- Linear Regression

---

## 3️⃣ Delay Reason Model
Predicts the possible reason for delay.

Possible predictions:
- Traffic
- Weather
- Restaurant Delay
- Rider Availability
- No Delay

**Model Used**
- Decision Tree Classifier

---

# ⚙️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Frontend
- HTML
- CSS

### Visualization
- Matplotlib

### Model Storage
- Joblib

---

# 📊 Model Evaluation

### Regression Metrics
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

### Classification Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report

---

# 📂 Project Structure


project
│
├── static
│ └── style.css
│
├── templates
│ └── index.html
│
├── app.py
├── delivery_time_model.joblib
├── delay_reason_model.joblib
├── prep_time_model.joblib
├── metrics.json
├── requirements.txt
└── README.md


---

# 🚀 How to Run the Project

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/delivery-time-prediction-ml-app.git
2️⃣ Go to the project directory
cd delivery-time-prediction-ml-app
3️⃣ Install required packages
pip install -r requirements.txt
4️⃣ Run the Flask application
python app.py
5️⃣ Open the web app

Open your browser and go to:

http://127.0.0.1:5000
🖥️ Web Application

The user provides the following inputs:

City

Restaurant

Distance

Number of items

Peak hour

Traffic level

Weather

Priority

The system predicts:

🍳 Preparation Time
🕒 Estimated Delivery Time
⚠️ Possible Delay Reason

📈 Future Improvements

Use real food delivery datasets

Add advanced ML models

Deploy the application online

Add map-based distance calculation

Integrate real-time traffic API

Improve UI design

👨‍💻 Author

Huzaifa

Machine Learning & AI Enthusiast