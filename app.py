from flask import Flask, render_template, request
import pandas as pd
import joblib
import random

app = Flask(__name__)

# ── Load models ──
model_time = joblib.load("delivery_time_model.joblib")
model_delay = joblib.load("delay_reason_model.joblib")
model_prep = joblib.load("prep_time_model.joblib")
support_model = joblib.load("chatbotsupport.joblib")


# ─────────────────────────────
# HOME PAGE
# ─────────────────────────────
@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html")


# ─────────────────────────────
# PREDICTION PAGE
# ─────────────────────────────
@app.route("/predict-page")
def predict_page():
    return render_template("index.html")


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
@app.route("/predict", methods=["POST"])
def predict():

    city = request.form["city"].lower()
    restaurant = request.form["restaurant"].lower()
    distance = float(request.form["distance"])
    items = int(request.form["items"])
    peak = int(request.form["peak"])
    traffic = request.form["traffic"].lower()
    weather = request.form["weather"].lower()

    prep_time = model_prep.predict(
        pd.DataFrame([[restaurant]], columns=["restaurant"])
    )

    input1 = pd.DataFrame(
        [[city, distance, items, peak, traffic, weather, prep_time[0], restaurant]],
        columns=[
            "city","distance_km","order_items","is_peak_hour",
            "traffic_level","weather","prep_time","restaurant"
        ],
    )

    input2 = pd.DataFrame(
        [[city, distance, traffic, weather]],
        columns=["city","distance_km","traffic_level","weather"]
    )

    delivery_time = model_time.predict(input1)
    delay_reason = model_delay.predict(input2)

    return render_template(
        "index.html",
        prep=round(prep_time[0],2),
        time=round(delivery_time[0],2),
        reason=delay_reason[0]
    )


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)