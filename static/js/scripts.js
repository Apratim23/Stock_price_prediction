// Function to predict using Linear Regression model
function predictLR() {
    const input = document.getElementById('lrInput').value;
    const features = input.split(',').map(Number);  // Split and convert to an array of numbers

    fetch('/predict_lr', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('lrResult').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to predict using LSTM model
function predictLSTM() {
    const input = document.getElementById('lstmInput').value;
    const features = input.split(',').map(Number);  // Split and convert to an array of numbers

    fetch('/predict_lstm', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('lstmResult').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
