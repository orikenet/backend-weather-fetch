from flask import Flask, jsonify
import requests
from flask_cors import CORS

# Create the Flask app
app = Flask(__name__)
CORS(app)
# Define a single GET endpoint
@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!"

API_KEY = "5e355514f1c33954b3833350be683767"

# GET endpoint with a dynamic path parameter
@app.route("/weather/<location_key>", methods=["GET"])
def weather(location_key):
    # Build the OpenWeatherMap API URL
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location_key,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    # Call the OpenWeatherMap API
    response = requests.get(url, params=params)

    # If successful, return JSON data, else return error
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "City not found or API error"}), response.status_code


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)