from flask import Flask, render_template, request
import pandas as pd
import joblib
import random

# ─────────────────────────────────────────
# Initialize Flask App
# ─────────────────────────────────────────
app = Flask(__name__)

# ─────────────────────────────────────────
# Load ML Models
# ─────────────────────────────────────────
model_time = joblib.load("delivery_time_model.joblib")
model_delay = joblib.load("delay_reason_model.joblib")
model_prep = joblib.load("prep_time_model.joblib")
support_model = joblib.load("chatbotsupport.joblib")

# ─────────────────────────────────────────
# Chatbot Responses
# ─────────────────────────────────────────
responses = {
    "greeting": [
        "Hello! Welcome to Zwiggy Support. How can I help you today?",
        "Hi there! I'm Zwiggy's support assistant. What seems to be the issue?"
    ],

    "order_status": [
        "You can track your order live in 'My Orders'.",
        "If your order is delayed please wait a few minutes."
    ],

    "cancel_order": [
        "Orders can be cancelled within 2 minutes of placing.",
        "If preparation started cancellation may not be possible."
    ],

    "wrong_order": [
        "Please report wrong order under 'My Orders > Report Issue'.",
        "We can arrange replacement or refund."
    ],

    "missing_items": [
        "Report missing items within 24 hours.",
        "Missing items are refunded after verification."
    ],

    "refund": [
        "Refunds take 5–7 business days.",
        "Refund will return to original payment method."
    ],

    "payment_issue": [
        "Failed payments auto-refund in 24-48 hours.",
        "Please share transaction ID for investigation."
    ],

    "delivery_agent": [
        "You can rate the delivery agent inside the app.",
        "Use in-app chat to contact the delivery agent."
    ],

    "restaurant_issue": [
        "Restaurants sometimes take longer during peak hours.",
        "You will be notified once the order is ready."
    ],

    "predict_time": [
        "Go to the Predict page and enter order details to estimate delivery time."
    ],

    "promo_code": [
        "Promo codes may expire or require minimum order value."
    ],

    "account_issue": [
        "Use 'Forgot Password' to reset your account."
    ],

    "app_issue": [
        "Try updating or reinstalling the Zwiggy app."
    ],

    "thanks": [
        "Happy to help! Anything else?"
    ],

    "goodbye": [
        "Goodbye! Have a great day 🍕"
    ]
}

# ─────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────

# Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html")


# Prediction Page
@app.route("/predict-page")
def predict_page():
    return render_template("index.html")


# Prediction Logic
@app.route("/predict", methods=["POST"])
def predict():

    city = request.form["city"].lower()
    restaurant = request.form["restaurant"].lower()
    distance = float(request.form["distance"])
    items = int(request.form["items"])
    peak = int(request.form["peak"])
    traffic = request.form["traffic"].lower()
    weather = request.form["weather"].lower()

    # Predict preparation time
    prep_time = model_prep.predict(
        pd.DataFrame([[restaurant]], columns=["restaurant"])
    )

    # Delivery time input
    input1 = pd.DataFrame(
        [[city, distance, items, peak, traffic, weather, prep_time[0], restaurant]],
        columns=[
            "city",
            "distance_km",
            "order_items",
            "is_peak_hour",
            "traffic_level",
            "weather",
            "prep_time",
            "restaurant",
        ],
    )

    # Delay reason input
    input2 = pd.DataFrame(
        [[city, distance, traffic, weather]],
        columns=["city", "distance_km", "traffic_level", "weather"],
    )

    delivery_time = model_time.predict(input1)
    delay_reason = model_delay.predict(input2)

    return render_template(
        "index.html",
        prep=round(prep_time[0], 2),
        time=round(delivery_time[0], 2),
        reason=delay_reason[0],
    )


# Support Chatbot Page
@app.route("/support", methods=["GET", "POST"])
def support():

    user_msg = ""
    bot_reply = ""

    if request.method == "POST":
        user_msg = request.form.get("user_input", "").strip()

        bot_reply = "I'm sorry, I didn't understand that. Could you rephrase?"

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


# ─────────────────────────────────────────
# Run App
# ─────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)