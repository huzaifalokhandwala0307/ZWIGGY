# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Preprocessing tools
from sklearn.preprocessing import StandardScaler,OneHotEncoder

# Evaluation metrics
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,accuracy_score,confusion_matrix,classification_report

# ML pipeline utilities
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

# ML models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

# For saving trained models
import joblib
import json

# Setting random seed for reproducibility
np.random.seed(42)

# Number of synthetic samples
n = 50000


# Possible categories for dataset
cities = ["bangalore", "mumbai", "delhi", "hyderabad", "chennai"]
traffic_levels = ["low", "medium", "high"]
weather_conditions = ["clear", "rainy", "foggy"]
restaurants = ["dominos", "kfc", "mcdonalds", "subway", "local_cafe"]


# Creating synthetic dataset
df = pd.DataFrame({
    "city": np.random.choice(cities, n),
    "distance_km": np.round(np.random.uniform(1, 20, n), 2),
    "order_items": np.random.randint(1, 8, n),
    "is_peak_hour": np.random.choice([0, 1], n, p=[0.6, 0.4]),
    "traffic_level": np.random.choice(traffic_levels, n, p=[0.3, 0.4, 0.3]),
    "weather": np.random.choice(weather_conditions, n, p=[0.7, 0.2, 0.1]),
    "restaurant" : np.random.choice(restaurants, n)
})


# Generating preparation time based on number of items
df["prep_time"] = np.round(
    10 + df["order_items"] * np.random.uniform(2, 5, n), 1
)


# Base delivery time calculation
df["delivery_time"] = (
    15
    + df["distance_km"] * np.random.uniform(1.8, 2.5, n)
    + df["prep_time"]
    + df["is_peak_hour"] * np.random.uniform(8, 15, n)
)


# Adding delay due to traffic
df.loc[df["traffic_level"] == "Medium", "delivery_time"] += np.random.uniform(
    5, 10, (df["traffic_level"] == "Medium").sum()
)

df.loc[df["traffic_level"] == "High", "delivery_time"] += np.random.uniform(
    10, 20, (df["traffic_level"] == "High").sum()
)


# Adding delay due to weather conditions
df.loc[df["weather"] == "Rainy", "delivery_time"] += np.random.uniform(
    5, 12, (df["weather"] == "Rainy").sum()
)

df.loc[df["weather"] == "Foggy", "delivery_time"] += np.random.uniform(
    8, 15, (df["weather"] == "Foggy").sum()
)


# Rounding delivery time
df["delivery_time"] = np.round(df["delivery_time"], 1)


# Function to generate delay reason (classification target)
def delay_reason(row):
    if row["traffic_level"] == "High":
        return "Traffic"
    elif row["prep_time"] > 30:
        return "Restaurant Delay"
    elif row["weather"] in ["Rainy", "Foggy"]:
        return "Weather"
    elif row["is_peak_hour"] == 1 and row["order_items"] > 5:
        return "Rider Availability"
    else:
        return "No Delay"


# Creating delay_reason column
df["delay_reason"] = df.apply(delay_reason, axis=1)


# Optional: Save dataset
# df.to_csv("delivery_app_dataset_500.csv", index=False)


# Print dataset columns
print(df.columns)


# Taking user input for prediction
i_city = input("Enter city: ")
i_restaurant = input("restaurant name : ")
i_distance_km = float(input("Enter distance (km): "))
i_order_items = int(input("Enter number of items: "))
i_is_peak_hour = int(input("Peak hour? (1=yes, 0=no): "))
i_traffic_level = input("Traffic level (Low/Medium/High): ")
i_weather = input("Weather (Clear/Rainy/Foggy): ")


# Dataset for preparation time prediction
x3 = df[['restaurant']]
y3 = df['prep_time']


# Creating dataframe for restaurant input
input_restaurant_df = pd.DataFrame([[i_restaurant]], columns=['restaurant'])


# Dataset for delivery time prediction
x1 = df[['city', 'distance_km', 'order_items', 'is_peak_hour', 'traffic_level','weather','prep_time','restaurant']]
y1 = df['delivery_time']


# Dataset for delay reason prediction
x2 = df[['city', 'distance_km', 'traffic_level','weather']]
y2 = df['delay_reason']


# Splitting datasets into training and testing
X1_train, X1_test, y1_train, y1_test = train_test_split(
    x1, y1, test_size=0.2, random_state=42
)

X_2train, X2_test, y2_train, y2_test = train_test_split(
    x2, y2, test_size=0.2, random_state=42
)


print(type(X1_train))


# Columns used for preprocessing (delivery time model)
cat_cols_1 = ['city', 'traffic_level', 'weather','restaurant']
num_cols_1 = ['distance_km', 'order_items', 'is_peak_hour', 'prep_time']


# ColumnTransformer for preprocessing
preprocess_1 = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols_1),
    ('num', StandardScaler(), num_cols_1)
])


# Pipeline for delivery time prediction
pipeline1 = Pipeline([
    ('preprocess', preprocess_1),
    ('model', LinearRegression())
])


# Columns for delay reason model
cat_cols_2 = ['city', 'traffic_level', 'weather']
num_cols_2 = ['distance_km']


# Preprocessing for classification model
preprocess_2 = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols_2),
    ('num', StandardScaler(), num_cols_2)
])


# Pipeline for delay reason prediction
pipeline2 = Pipeline([
    ('preprocess', preprocess_2),
    ('model', DecisionTreeClassifier(max_depth=5, min_samples_leaf=10))
])


# Preprocessing for preparation time model
preprocess_3 = ColumnTransformer([
     ('cat', OneHotEncoder(handle_unknown='ignore'), ['restaurant'])
])


# Pipeline for preparation time prediction
pipeline3 = Pipeline([
    ('preprocess', preprocess_3),
    ('model', LinearRegression())
])


# Training the models
pipeline1.fit(X1_train, y1_train)
pipeline2.fit(X_2train, y2_train)
pipeline3.fit(x3,y3)


# Predict preparation time
prep_time = pipeline3.predict(pd.DataFrame([[i_restaurant]],columns = ["restaurant"]))


# Input for delivery time prediction
input_1 = [
    i_city.lower(),
    i_restaurant.lower(),
    i_distance_km,
    i_order_items,
    i_is_peak_hour,
    i_traffic_level.lower(),
    i_weather.lower(),
    prep_time
]


# Creating dataframe for delivery time prediction
input_1_df = pd.DataFrame(
    [input_1],
    columns=['city', 'restaurant','distance_km', 'order_items',
             'is_peak_hour', 'traffic_level', 'weather', 'prep_time']
)


# Input for delay reason prediction
input_2 = [
    i_city.lower(),
    i_distance_km,
    i_traffic_level.lower(),
    i_weather.lower()
]


# Creating dataframe for delay reason prediction
input_2_df = pd.DataFrame(
    [input_2],
    columns=['city', 'distance_km', 'traffic_level', 'weather']
)


# Predict delivery time and delay reason
time  = pipeline1.predict(input_1_df)
reason = pipeline2.predict(input_2_df)


# Display prediction results
print("📦 Delivery Prediction Result")
print(f"🍳 Your preperation time will be : {round(prep_time[0],2)} minitues")
print(f"🕒 Estimated Time : {round(time[0], 2)} minutes")
print(f"⚠️ Delay Reason  : {reason[0]}")


# Evaluate delivery time model
y1_pred = pipeline1.predict(X1_test)

mse = mean_squared_error(y1_test, y1_pred)
rmse = mse**(1/2)
mae = mean_absolute_error(y1_test, y1_pred)
r2 = r2_score(y1_test, y1_pred)

print("MSE :", mse)
print("RMSE:", rmse)
print("MAE :", mae)
print("R²  :", r2)

print()


# Evaluate classification model
y2_pred = pipeline2.predict(X2_test)

acc = accuracy_score(y2_test, y2_pred)
conf_matrix = confusion_matrix(y2_test, y2_pred)

print("accuracy_score is : ",acc)
print("confusion_matrix is : ",conf_matrix)
print(classification_report(y2_test, y2_pred))

# Overall score (average of R² and accuracy)
overall_score = (r2 + acc) / 2
print("Overall Model Score:", overall_score)

# Visualization: Actual vs Predicted delivery time
plt.figure()
plt.scatter(y1_test, y1_pred)

plt.plot([y1_test.min(), y1_test.max()],
         [y1_test.min(), y1_test.max()],
         label="Ideal Fit (y = x)")

plt.xlabel("Actual Delivery Time")
plt.ylabel("Predicted Delivery Time")
plt.title("Actual vs Predicted Delivery Time")

plt.grid()
plt.legend()
plt.show()


# Saving trained models
joblib.dump(pipeline1, "delivery_time_model.joblib")
joblib.dump(pipeline2, "delay_reason_model.joblib")
joblib.dump(pipeline3, "prep_time_model.joblib")

# Save metrics
with open("metrics.json", "w") as f:
    json.dump({"r2": r2, "acc": acc, "overall": overall_score}, f)
