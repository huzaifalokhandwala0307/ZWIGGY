# 🍔 Zwiggy – Smart Food Delivery Prediction App

Zwiggy is a **Flask-based web application** that predicts food delivery time using **Machine Learning**.  
The app simulates a modern food delivery platform where users can browse restaurants, predict delivery time, and get support through a chatbot.

---

## 🚀 Features

- 🧠 **Machine Learning Delivery Prediction**
  - Predicts delivery time based on:
    - City
    - Restaurant
    - Distance
    - Number of items
    - Traffic level
    - Weather conditions
    - Peak hour

- 🍽 **Restaurant Selection**
  - Choose from restaurants like:
    - Dominos
    - KFC
    - McDonald's
    - Subway
    - Local Cafe

- 🤖 **Customer Support Chatbot**
  - AI-based chatbot to assist users with common delivery queries.

- 🌐 **Multi-Page Web Application**
  - Home page
  - Restaurant pages
  - Delivery prediction page
  - Customer support page

- 🎨 **Modern UI**
  - Swiggy-inspired design
  - Responsive layout
  - Clean restaurant cards

---

## 🧠 Machine Learning Models Used

| Model | Purpose |
|------|--------|
| Linear Regression | Predict delivery time |
| Decision Tree Classifier | Predict delay reason |
| NLP Model | Chatbot intent classification |

---

## 🛠 Tech Stack

**Frontend**
- HTML5
- CSS3
- JavaScript (planned)

**Backend**
- Python
- Flask

**Machine Learning**
- Scikit-learn
- Pandas
- NumPy

**Model Storage**
- Joblib

---

## 📂 Project Structure


Zwiggy/
│
├── static/
│ ├── base.css
│ ├── dominos.css
│ ├── kfc.css
│ ├── subway.css
│ ├── localcafe.css
│ ├── mcdonalds.svg
│ ├── subway.svg
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── support.html
│ ├── dominos.html
│ ├── kfc.html
│ ├── mcdonald.html
│ ├── subway.html
│ ├── localcafe.html
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


---

## ⚙️ Installation

### 1️⃣ Clone the repository
git clone https://github.com/huzaifalokhandwala0307/ZWIGGY.git 
cd zwiggy
2️⃣ Install dependencies
pip install -r Requirement.txt
3️⃣ Run the application
python app.py
4️⃣ Open in browser
http://127.0.0.1:5000
📊 Example Prediction

Input parameters:

City: Bangalore

Restaurant: Dominos

Distance: 5 km

Items: 3

Traffic: Medium

Weather: Clear

Output:

Preparation Time: 18 minutes
Estimated Delivery Time: 42 minutes
Delay Reason: No Delay
🔮 Future Improvements

🛒 Add cart and ordering system

📍 Integrate map-based distance calculation

📦 Real-time order tracking simulation

💳 Payment integration

🗄 Database integration (SQLite / PostgreSQL)

📱 Fully responsive mobile UI

👨‍💻 Author

Huzaifa

Machine Learning & Web Development Enthusiast

⭐ Project Status

🚧 In Development
New features such as JavaScript interactivity and database integration will be added soon.

📜 License

This project is open source and available under the MIT License.


---

✅ This README will make your **GitHub project look professional**.

If you want, I can also give you a **better GitHub project title + description + tags** so your repo looks even stronger.

This project is open source and available under the **MIT License**.

whats this

That line in the README:

“This project is open source and available under the MIT License.”

means people are allowed to use your project code under certain rules.

📜 What an MIT License Means

The MIT License is a very simple open-source license.

If you publish your project with it, others can:

✅ Use your code
✅ Modify your code
✅ Share your code
✅ Use it in their own projects (even commercial ones)

But they must:

Keep your copyright notice

Mention the MIT license

Example

Someone could take your Zwiggy project, improve it, and build a bigger app from it — but they must still mention you as the original author.

Do you actually need it?

For college / portfolio projects, it's optional.

You have 3 choices:

1️⃣ MIT License (most common for GitHub projects)
2️⃣ No license – people technically cannot reuse your code
3️⃣ Private repo – only you see it

If you want to use MIT License

Create a file called:

LICENSE

Then add:

MIT License

Copyright (c) 2026 Huzaifa
