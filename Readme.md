# 🍔 Zwiggy – ML-Powered Food Delivery Web App

Zwiggy is a full-stack food delivery web application inspired by platforms like Swiggy & Zomato, enhanced with a Machine Learning model to predict delivery time dynamically.

> 🚀 **A real-world inspired project combining Frontend + Backend + Machine Learning into one system.**

---

## 🚀 Live Features

### 🍽️ Food Ordering UI

* Multiple restaurant pages (McDonald's, Dominos, KFC, Subway)
* Clean and responsive design
* Real-world inspired layout

### 🛒 Smart Cart System

* Add items dynamically to cart
* Increase / decrease quantity
* Automatic total price calculation
* Interactive side cart panel
* “Place Order” functionality

### ⚡ JavaScript Interactivity

* Real-time UI updates
* Dynamic cart rendering
* Smooth user experience

### 🧠 ML-Based Delivery Prediction

* Predicts estimated delivery time
* Based on:

  * Distance
  * Traffic conditions
  * Order details
* Integrated with Flask backend

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python (Flask)

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

---

## 📂 Project Structure

```bash
zwiggy/
│── static/
│   ├── dominos.css
│   ├── kfc.css
│   ├── subway.css
│   ├── style.css
│   ├── main.js
│
│── templates/
│   ├── index.html
│   ├── dominos.html
│   ├── kfc.html
│   ├── subway.html
│   ├── mcdonald.html
│
│── app.py
│── predict_time.py
│── delivery_time_model.joblib
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/zwiggy.git
cd zwiggy
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧠 Machine Learning Details

The delivery time prediction model uses regression techniques to estimate delivery duration.

### Features used:

* Distance
* Traffic conditions
* Preparation time

### Workflow:

1. Data preprocessing (encoding + scaling)
2. Model training
3. Model saved using `.joblib`
4. Integrated into Flask backend

---

## 🔥 Future Enhancements

* 💾 Save cart using localStorage
* 📦 Order confirmation page
* ⏱️ Real-time delivery tracking simulation
* 🔐 User authentication system
* ☁️ Deploy to cloud (Render / Vercel)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📬 Contact

* 💼 LinkedIn: https://www.linkedin.com/in/huzaifa-lokhandwalala-ab5b21375

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 💡 Project Goal

To build a real-world inspired full-stack application that combines:

* Frontend development
* Backend integration
* Machine Learning

into a single impactful product.
