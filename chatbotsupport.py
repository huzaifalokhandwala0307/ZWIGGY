from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np
import pandas as pd
import random
import joblib

# ── Zwiggy Support Intent Patterns ──
intent_patterns = {

    "greeting": [
        "hi", "hello", "hey", "good morning", "good evening",
        "hey there", "yo", "hello zwiggy", "hi zwiggy"
    ],

    "order_status": [
        "where is my order", "track my order", "order status",
        "how long will my order take", "is my order on the way",
        "when will my food arrive", "my order is late",
        "i have not received my order", "order not delivered yet"
    ],

    "cancel_order": [
        "cancel my order", "i want to cancel", "how to cancel order",
        "cancel the order i just placed", "stop my order",
        "i dont want my order anymore"
    ],

    "wrong_order": [
        "i got the wrong order", "wrong food delivered",
        "my order is incorrect", "received wrong items",
        "this is not what i ordered", "wrong restaurant order"
    ],

    "missing_items": [
        "items are missing from my order", "something is missing",
        "i did not get all my items", "missing food in my order",
        "order incomplete", "part of my order is missing"
    ],

    "refund": [
        "i want a refund", "how do i get a refund",
        "refund my money", "when will i get my refund",
        "refund not received", "i want my money back"
    ],

    "payment_issue": [
        "payment failed", "my payment did not go through",
        "i was charged but order not placed", "double charged",
        "payment issue", "money deducted but no order"
    ],

    "delivery_agent": [
        "delivery agent is not responding", "agent is rude",
        "delivery boy is late", "contact delivery agent",
        "agent phone not reachable", "rider behaviour complaint"
    ],

    "restaurant_issue": [
        "restaurant is taking too long", "restaurant not accepting order",
        "restaurant cancelled my order", "food quality is bad",
        "restaurant is closed", "food was cold"
    ],

    "predict_time": [
        "how long will delivery take", "estimate delivery time",
        "what is the delivery time", "predict my delivery",
        "how fast will my order arrive", "delivery time estimate"
    ],

    "promo_code": [
        "my promo code is not working", "coupon not applied",
        "discount not applied", "promo code invalid",
        "how to apply coupon", "offer not working"
    ],

    "account_issue": [
        "i cannot login", "forgot my password", "reset my password",
        "account is blocked", "change my phone number",
        "update my address", "edit my profile"
    ],

    "app_issue": [
        "app is not working", "zwiggy app is crashing",
        "app keeps closing", "cannot open the app",
        "app is slow", "error on app"
    ],

    "thanks": [
        "thank you", "thanks", "thanks a lot",
        "that helped", "great help", "you are helpful"
    ],

    "goodbye": [
        "bye", "goodbye", "see you", "talk later",
        "that is all", "no more questions"
    ]
}


# ── Variation Generator (same as your original) ──
def generate_variation(text):
    variations = [
        text,
        text + " please",
        "zwiggy " + text,
        text + " help",
        "can you help with " + text,
        "please " + text,
        "i need help with " + text,
        "i have a problem " + text,
    ]
    return random.choice(variations)


# ── Generate Training Data ──
data = []
for intent, phrases in intent_patterns.items():
    for _ in range(50):   # 50 samples per intent for better accuracy
        phrase = random.choice(phrases)
        new_text = generate_variation(phrase)
        data.append((new_text, intent))

df_intent = pd.DataFrame(data, columns=["text", "intent"])
print("Total training samples:", len(df_intent))


# ── Response Bank ──
df_response = pd.DataFrame({
    "intent": [
        "greeting", "greeting", "greeting",

        "order_status", "order_status", "order_status",

        "cancel_order", "cancel_order",

        "wrong_order", "wrong_order",

        "missing_items", "missing_items",

        "refund", "refund",

        "payment_issue", "payment_issue",

        "delivery_agent", "delivery_agent",

        "restaurant_issue", "restaurant_issue",

        "predict_time",

        "promo_code", "promo_code",

        "account_issue", "account_issue",

        "app_issue", "app_issue",

        "thanks", "thanks",

        "goodbye"
    ],
    "response": [
        # greeting
        "Hello! Welcome to Zwiggy Support. How can I help you today?",
        "Hi there! I'm Zwiggy's support assistant. What seems to be the issue?",
        "Hey! Zwiggy support here. Tell me what's going on and I'll sort it out.",

        # order_status
        "You can track your order live on the Zwiggy app under 'My Orders'. It shows real-time delivery status.",
        "Your order status is available in the app. If it says 'Out for Delivery', your rider is on the way!",
        "If your order is taking longer than expected, please wait 10 more minutes. If still delayed, I can escalate it.",

        # cancel_order
        "You can cancel your order within 2 minutes of placing it from the 'My Orders' section in the app.",
        "If the restaurant has already started preparing, cancellation may not be possible. Want me to check?",

        # wrong_order
        "I'm sorry about that! Please go to 'My Orders' > 'Report an Issue' > 'Wrong Order' and we'll resolve it.",
        "That's not okay! Please report the wrong order in the app and we'll arrange a replacement or refund.",

        # missing_items
        "Sorry about the missing items! Please report it under 'My Orders' > 'Report Issue' and we'll refund the missing items.",
        "Missing items are always refunded. Use the app to report within 24 hours of delivery.",

        # refund
        "Refunds are processed within 5 – 7 business days to your original payment method.",
        "If your refund is taking longer than 7 days, please share your order ID and I'll escalate it.",

        # payment_issue
        "If money was deducted but order wasn't placed, don't worry — it will auto-refund within 24–48 hours.",
        "For double charge issues, please share your transaction ID and we'll investigate immediately.",

        # delivery_agent
        "I'm sorry about that experience. Please rate your delivery agent in the app and flag the issue — we take this seriously.",
        "If the agent is unreachable, you can contact them via the app's in-built chat or call feature.",

        # restaurant_issue
        "If the restaurant is taking too long, it's often due to high demand. You'll get a notification when food is ready.",
        "Food quality complaints can be reported under 'My Orders' > 'Rate Order'. We review all feedback.",

        # predict_time
        "Want to predict your delivery time? Head over to our Predict Delivery page — just enter your order details and we'll estimate it for you!",

        # promo_code
        "Promo codes are case-sensitive and may have expiry dates or minimum order requirements. Double-check those!",
        "If a valid promo code isn't working, try removing it and re-entering. If still failing, I'll raise a ticket.",

        # account_issue
        "To reset your password, go to the login page and tap 'Forgot Password'. A reset link will be sent to your email.",
        "For account or profile issues, go to Settings > Account Info. If you're blocked, contact us with your registered phone number.",

        # app_issue
        "Try clearing the app cache or reinstalling Zwiggy. Make sure you're on the latest version.",
        "App crashes are usually fixed by updating or reinstalling. If the issue persists, share your device model and we'll investigate.",

        # thanks
        "Happy to help! Is there anything else I can assist you with?",
        "Glad I could help! Have a great day and enjoy your meal! 🛵",

        # goodbye
        "Goodbye! Thank you for contacting Zwiggy Support. Have a wonderful day! 🍕"
    ]
})


# ── Train Model (same pipeline as your original) ──
z = df_intent["intent"]
x = df_intent["text"]

X_train, X_test, z_train, z_test = train_test_split(
    x, z, test_size=0.2, random_state=42
)

p1 = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", LogisticRegression(max_iter=300))
])

p1.fit(X_train, z_train)
print("Model trained successfully!\n")
print("=" * 45)
print("       ZWIGGY SUPPORT ASSISTANT")
print("=" * 45)
print("Type your issue below. Type 'bye' to exit.\n")


# ── Chat Loop (same structure as your original) ──
exit_phrases = np.array([
    "bye", "goodbye", "see you", "exit",
    "quit", "that is all", "no more questions"
])

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    print(f"You: {user_input}")

    if user_input.lower() in exit_phrases:
        print("Zwiggy Support: Goodbye! Thank you for contacting Zwiggy Support. Have a great day! 🛵")
        break

    predicted_intent = p1.predict([user_input])[0]
    responses = df_response[df_response["intent"] == predicted_intent]["response"].values

    if len(responses) > 0:
        print(f"Zwiggy Support: {random.choice(responses)}\n")
    else:
        print("Zwiggy Support: I'm sorry, I didn't understand that. Could you rephrase?\n")


# ── Model Evaluation (same as your original) ──
ypred = p1.predict(X_test)

acc = accuracy_score(z_test, ypred)
print("\nAccuracy of model:", round(acc, 2))
print()

con = confusion_matrix(z_test, ypred)
print("Confusion Matrix:")
print(con)
print()

cl = classification_report(z_test, ypred)
print("Classification Report:\n", cl)

#save model
joblib.dump(p1, "chatbotsupport.joblib")
print("model saved" )