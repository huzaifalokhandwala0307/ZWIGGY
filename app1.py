from flask import Flask, render_template, request
import pandas as pd
import joblib, json

# Initialize Flask app
app = Flask(__name__)

# Load trained models
model_time = joblib.load("delivery_time_model.joblib")
model_delay = joblib.load("delay_reason_model.joblib")
model_prep = joblib.load("prep_time_model.joblib")

# Load precomputed metrics (saved during training)
with open("metrics.json") as f:
    metrics = json.load(f)
overall_accuracy = metrics["overall"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Collect form inputs
    city = request.form["city"].lower()
    restaurant = request.form["restaurant"].lower()
    distance = float(request.form["distance"])
    items = int(request.form["items"])
    peak = int(request.form["peak"])
    traffic = request.form["traffic"].lower()
    weather = request.form["weather"].lower()

    # Predict preparation time
    prep_time = model_prep.predict(pd.DataFrame([[restaurant]], columns=["restaurant"]))

    # Input for delivery time model
    input1 = pd.DataFrame(
        [[city, distance, items, peak, traffic, weather, prep_time[0], restaurant]],
        columns=[
            "city","distance_km","order_items","is_peak_hour",
            "traffic_level","weather","prep_time","restaurant"
        ]
    )

    # Input for delay reason model
    input2 = pd.DataFrame(
        [[city, distance, traffic, weather]],
        columns=["city","distance_km","traffic_level","weather"]
    )

    # Predictions
    delivery_time = model_time.predict(input1)
    delay_reason = model_delay.predict(input2)

    # Render results
    return render_template(
        "index.html",
        prep=round(prep_time[0], 2),
        time=round(delivery_time[0], 2),
        reason=delay_reason[0],
        accuracy=round(overall_accuracy * 100, 2)  # percentage
    )

if __name__ == "__main__":
    app.run(debug=True)
