import joblib
import tensorflow as tf
from tensorflow.keras.losses import MeanSquaredError
from flask import Flask, request, jsonify, render_template
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained models
lr_model = joblib.load("models/linear_regression.pkl")
lstm_model = tf.keras.models.load_model(
    "models/lstm_model.h5",
    custom_objects={"mse": MeanSquaredError()}  # Register custom loss function
)

# Load the scaler
scaler = joblib.load("models/scaler.pkl")

# Serve index.html on the root route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_lr", methods=["POST"])
def predict_lr():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)

    # Scale the input features
    scaled_features = scaler.transform(features)
    
    # Predict using Linear Regression
    prediction = lr_model.predict(scaled_features)
    return jsonify({"prediction": prediction.tolist()})

@app.route("/predict_lstm", methods=["POST"])
def predict_lstm():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1, 1)  # Reshape for LSTM input

    # Scale the input features
    scaled_features = scaler.transform(features.reshape(1, -1))

    # Predict using LSTM model
    prediction = lstm_model.predict(scaled_features.reshape(1, -1, 1))
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
