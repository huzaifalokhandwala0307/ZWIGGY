# 🍔 Zwiggy – Smart Food Delivery Prediction App

Zwiggy is a **Flask-based web application** that predicts food delivery time using **Machine Learning**.
The application simulates a modern food delivery platform where users can browse restaurants, estimate delivery time, and get assistance through a chatbot.

---

# 🚀 Features

### 🧠 Machine Learning Delivery Prediction

Predict delivery time based on:

* City
* Restaurant
* Distance
* Number of items
* Traffic level
* Weather conditions
* Peak hour

### 🍽 Restaurant Selection

Users can browse restaurants such as:

* Dominos
* KFC
* McDonald's
* Subway
* Local Cafe

### 🤖 Customer Support Chatbot

An AI-powered chatbot that helps users with common delivery issues like:

* Order status
* Refunds
* Missing items
* Payment issues

### 🌐 Multi-Page Web Application

The application includes:

* Home page
* Restaurant pages
* Delivery prediction page
* Customer support page

### 🎨 Modern UI

* Swiggy-inspired design
* Clean restaurant cards
* Simple navigation system

---

# 🧠 Machine Learning Models

| Model                    | Purpose                   |
| ------------------------ | ------------------------- |
| Linear Regression        | Predict delivery time     |
| Decision Tree Classifier | Predict delay reason      |
| NLP Intent Model         | Support chatbot responses |

---

# 🛠 Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript *(planned)*

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

## Model Storage

* Joblib

---

# 📂 Project Structure

```
zwiggy/
│
├── static/
│   ├── base.css
│   ├── dominos.css
│   ├── kfc.css
│   ├── subway.css
│   ├── localcafe.css
│   ├── support.css
│   ├── mcdonalds.svg
│   ├── subway.svg
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── support.html
│   ├── dominos.html
│   ├── kfc.html
│   ├── mcdonald.html
│   ├── subway.html
│   ├── localcafe.html
│
├── app.py
├── predict_time.py
├── chatbotsupport.py
│
├── delivery_time_model.joblib
├── delay_reason_model.joblib
├── prep_time_model.joblib
│
├── Requirement.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/huzaifalokhandwala0307/ZWIGGY.git
cd zwiggy-delivery-prediction
```

### 2️⃣ Install Dependencies

```
pip install -r Requirement.txt
```

### 3️⃣ Run the Flask Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

# 📊 Example Prediction

Input parameters:

City: Bangalore
Restaurant: Dominos
Distance: 5 km
Items: 3
Traffic: Medium
Weather: Clear

Output:

```
Preparation Time: 18 minutes
Estimated Delivery Time: 42 minutes
Delay Reason: No Delay
```

---

# 🔮 Future Improvements

Planned improvements for the project:

* Add JavaScript interactivity
* Add cart and order simulation
* Integrate database (SQLite / PostgreSQL)
* Add real-time order tracking simulation
* Improve responsive mobile UI
* Add restaurant menus and pricing

---

# 👨‍💻 Author

Huzaifa

Machine Learning & Web Development Enthusiast

---

# ⭐ Project Status

🚧 Active Development

New features such as **JavaScript functionality and database integration** will be added soon.

---

# 📜 License

This project is open-source and available under the **MIT License**.
