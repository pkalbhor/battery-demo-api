from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
api = Api(app)

class BatteryData(Resource):
    def get(self):
        # Example response, replace with actual data retrieval logic
        return {
            "status": "success",
            "data": {
                "voltage": 3.7,
                "current": 1.2,
                "temperature": 25.0
            }
        }, 200

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
    app.run(debug=True, port=8080)