from flask import Flask, request, jsonify
from flask_cors import CORS
from engine.decision_engine import DecisionEngine
from db.firestore_repo import FirestoreRepo
from firebase.auth_middleware import check_auth
from services.market_service import MarketService
from services.sensor_service import SensorService
from config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Init Services
engine = DecisionEngine()
repo = FirestoreRepo()
market_svc = MarketService()
sensor_svc = SensorService()

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "mode": "Live"}), 200

@app.route('/analyze', methods=['POST', 'OPTIONS'])
@check_auth
def analyze_crop():
    if request.method == 'OPTIONS': return jsonify({}), 200
    try:
        data = request.json
        result = engine.analyze(data)
        if hasattr(request, 'user'):
            repo.save_analysis(request.user.get('uid'), result)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- NEW ENDPOINTS ---
@app.route('/market', methods=['GET'])
def get_market():
    return jsonify(market_svc.get_trends()), 200

@app.route('/sensors', methods=['GET'])
def get_sensors():
    return jsonify(sensor_svc.get_readings()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)