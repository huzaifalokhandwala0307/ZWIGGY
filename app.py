from flask import Flask, render_template, request, jsonify, session, redirect
import pandas as pd
import joblib
import random
import os
import datetime
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.secret_key = "super_secret_zwiggy_key_123"

# Initialize Firebase Admin
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(os.environ.get("FIREBASE_CREDENTIALS_PATH", "firebase-key.json"))
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print("Firebase init error:", e)

try:
    db = firestore.client()
except:
    db = None

# ── Load models ──
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_time = joblib.load(os.path.join(BASE_DIR, "delivery_time_model.joblib"))
model_delay = joblib.load(os.path.join(BASE_DIR, "delay_reason_model.joblib"))
model_prep = joblib.load(os.path.join(BASE_DIR, "prep_time_model.joblib"))
support_model = joblib.load(os.path.join(BASE_DIR, "chatbotsupport.joblib"))


# ─────────────────────────────
# HOME PAGE
# ─────────────────────────────
@app.route("/")
def root():
    return redirect("/login")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/set-user", methods=["POST"])
def set_user():
    data = request.json
    session["user"] = data
    return {"status": "ok"}

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")


# ─────────────────────────────
# ─────────────────────────────

# RESTAURANT PAGES
# ─────────────────────────────
@app.route("/dominos")
def dominos():
    return render_template("dominos.html")

@app.route("/kfc")
def kfc():
    return render_template("kfc.html")

@app.route("/mcdonalds")
def mcdonalds():
    return render_template("mcdonald.html")

@app.route("/subway")
def subway():
    return render_template("subway.html")

@app.route("/localcafe")
def local_cafe():
    return render_template("localcafe.html")


# ─────────────────────────────
# DELIVERY PREDICTION
# ─────────────────────────────
@app.route("/predict", methods=["GET"])
def predict_page():
    return render_template("predict.html")


# ─────────────────────────────
# SUPPORT CHATBOT
# ─────────────────────────────
@app.route("/support", methods=["GET","POST"])
def support():

    responses = {
        "greeting": [
            "Hello! Welcome to Zwiggy Support.",
            "Hi! How can I help you today?"
        ],
        "order_status": [
            "You can track your order in the 'My Orders' section.",
            "Your order should arrive shortly!"
        ],
        "refund": [
            "Refunds usually take 5–7 business days.",
            "Your refund will return to the original payment method."
        ],
        "cancel_order": [
            "Orders can only be cancelled within 2 minutes after placing."
        ],
        "thanks": [
            "Happy to help!",
            "Glad I could help!"
        ],
        "goodbye": [
            "Goodbye! Have a great day!"
        ]
    }

    user_msg = ""
    bot_reply = ""

    if request.method == "POST":
        user_msg = request.form.get("user_input","").strip()

        bot_reply = "I'm sorry, I didn't understand that."

        if user_msg:
            predicted_intent = support_model.predict([user_msg])[0]
            intent_responses = responses.get(predicted_intent, [])

            if intent_responses:
                bot_reply = random.choice(intent_responses)

    return render_template(
        "support.html",
        user_msg=user_msg,
        bot_reply=bot_reply
    )

# ─────────────────────────────
# FIREBASE & RAZORPAY API
# ─────────────────────────────
@app.route("/api/config")
def api_config():
    return jsonify({
        "firebase": {
            "apiKey": os.environ.get("FIREBASE_API_KEY", ""),
            "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN", ""),
            "projectId": os.environ.get("FIREBASE_PROJECT_ID", ""),
            "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET", ""),
            "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID", ""),
            "appId": os.environ.get("FIREBASE_APP_ID", "")
        }
    })

@app.route("/save-user", methods=["POST"])
def save_user():
    data = request.json
    uid = data.get("uid")
    if uid and db:
        try:
            db.collection("users").document(uid).set({
                "uid": uid,
                "name": data.get("name"),
                "email": data.get("email"),
                "last_login": datetime.datetime.now()
            }, merge=True)
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Invalid data or DB offline"}), 400

@app.route("/place-order", methods=["POST"])
def place_order():
    data = request.json
    print("ORDER RECEIVED:", data)
    return {
        "status": "success",
        "message": "Order placed successfully"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)