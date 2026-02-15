import firebase_admin
from firebase_admin import credentials, firestore, auth
from config import Config
import os

def initialize_firebase():
    """
    Initializes Firebase Admin SDK.
    Returns the Firestore client if successful, else None.
    """
    try:
        if Config.OFFLINE_MODE:
            print("Offline Mode: Firebase initialization skipped.")
            return None

        cred_path = Config.FIREBASE_CREDENTIALS_PATH
        
        if not cred_path or not os.path.exists(cred_path):
            print(f"Warning: Firebase credentials not found at {cred_path}. Firestore disabled.")
            return None

        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            
        print("Firebase initialized successfully.")
        return firestore.client()
    except Exception as e:
        print(f"Firebase Init Error: {e}")
        return None

# Global DB Instance
db = initialize_firebase()