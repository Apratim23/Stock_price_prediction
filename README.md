# Stock Price Prediction Web Application

Welcome to the **Stock Price Prediction Web Application**, a tool built using **Flask**, **Machine Learning** models (Linear Regression and LSTM), and a sleek **Frontend** for seamless interaction. This app predicts stock prices based on historical data using two powerful prediction models: **Linear Regression** and **LSTM (Long Short-Term Memory)**.

## 🚀 **Features**
- **Linear Regression Model**: Predict stock prices using a traditional machine learning model.
- **LSTM Model**: Predict stock prices using a deep learning model designed for time-series data.
- **Interactive Web Interface**: Easily enter stock price data and get predictions with just a click.
- **Backend with Flask**: A lightweight backend for processing the predictions and returning results in real-time.
  
## 🛠️ **Technologies Used**
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Backend**: Flask, Python
- **Machine Learning Models**:
  - **Linear Regression**: A classical machine learning approach for regression tasks.
  - **LSTM**: A deep learning model, perfect for time-series prediction.
- **Model Serialization**: `joblib` for Linear Regression and `h5` format for LSTM model storage.

## 🌟 **Getting Started**

### Prerequisites

Before you begin, make sure you have the following installed:

1. **Python 3.x** (Recommended: Python 3.8 or above)
2. **pip** (Python's package installer)

### Clone the Repository

```bash
git clone https://github.com/your-username/stock-price-prediction.git
cd stock-price-prediction
```

### Install Dependencies

Use the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries, including Flask, TensorFlow, scikit-learn, and others.

### Directory Structure
```
stock-price-prediction/
├── app.py              # Backend Flask application
├── models/             # Contains trained models (LSTM, Linear Regression, Scaler)
│   ├── lstm_model.h5
│   ├── linear_regression.pkl
│   └── scaler.pkl
├── templates/          # Frontend HTML files
│   └── index.html
├── static/             # Frontend CSS and JS files
│   ├── styles.css
│   └── script.js
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation
```

### Running the Application

To run the application locally, use the following command:

```bash
python app.py
```

Once the Flask server starts, navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

### Using the Application

1. **Input**: Enter the historical stock price data in the input box (comma-separated values).
   Example: `120.50, 121.30, 122.10, 123.00, 124.50`

2. **Select Model**: Choose either the **Linear Regression** or **LSTM** model.

3. **Predict**: Click on the "Predict" button to get the stock price prediction.

4. **Result**: View the predicted stock price directly on the web page.

## 🧑‍💻 **How It Works**

- The **Linear Regression** model is trained using historical stock price data and makes predictions based on past trends.
  
- The **LSTM** model, a type of Recurrent Neural Network (RNN), is specifically designed for sequential data like stock prices. It learns patterns from historical prices and predicts future trends.

- **Flask** acts as the web framework to handle requests and serve the models' predictions. The backend interacts with the models and returns the results as JSON, which is displayed to the user in the frontend.

## 🏗️ **Frontend**
The frontend is designed to be simple and user-friendly:

- **HTML**: Provides the structure of the page.
- **CSS**: Adds styling to create an attractive and easy-to-use interface.
- **JavaScript**: Handles the user input, sends requests to the backend, and displays the predictions.

## ⚡ **Predictions Using the Models**

- **Linear Regression**: Provides a quick, linear approach to stock price prediction. It works best when the stock price follows a linear trend over time.
- **LSTM**: This deep learning model is ideal for time-series predictions like stock prices. It captures the complex patterns in data by considering previous time steps, making it a robust choice for predicting future prices.

## 💡 **Contributing**
We welcome contributions! If you would like to help improve this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## 📄 **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 **Contact**
For any questions, suggestions, or inquiries, feel free to contact me at:  
**Email**: apratimdutta.2003@gmail.com  
**GitHub**: [@Apratim23](https://github.com/Apratim23)

---

Feel free to modify or add additional information as needed! This structure is designed to give potential users and contributors clear instructions on how to use, test, and contribute to the project.
