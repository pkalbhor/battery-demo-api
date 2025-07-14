import csv
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
api = Api(app)

class BatteryData(Resource):
    def get(self):
        data = {
            "soc": [],
            "voltage": [],
            "current": [],
            "timestamp": []
        }
        try:
            with open('battery_data_kaggle.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Append values to respective lists, converting to float where appropriate
                    data["voltage"].append(float(row.get('voltage', 0)))
                    data["current"].append(float(row.get('current', 0)))
                    data["soc"].append(float(row.get('soc', 0)))
                    data["timestamp"].append(row.get('timestamp', ""))  # Keep as string
            return {
                "status": "success",
                "data": data
            }, 200
        except FileNotFoundError:
            return {
                "status": "error",
                "message": "battery_data_kaggle.csv file not found"
            }, 404
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }, 500

# Home page route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Battery API!",
        "available_endpoints": [
            {"endpoint": "/battery-data", "methods": ["GET"]}
        ]
    })

api.add_resource(BatteryData, '/battery-data')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)