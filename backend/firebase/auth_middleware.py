from functools import wraps
from flask import request, jsonify
from firebase_admin import auth
from config import Config

def check_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # --- FIX: Allow Browser Preflight (CORS) ---
        if request.method == 'OPTIONS':
            return f(*args, **kwargs)
        
        # Allow bypass in offline mode for testing
        if Config.OFFLINE_MODE:
            request.user = {"uid": "offline_user", "email": "test@agrosense.local"}
            return f(*args, **kwargs)

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Unauthorized. Missing token."}), 401

        token = auth_header.split(' ')[1]
        try:
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token 
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": "Invalid token", "details": str(e)}), 403
            
    return decorated_function