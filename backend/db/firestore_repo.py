from firebase.firebase_init import db
from config import Config
import datetime

class FirestoreRepo:
    def __init__(self):
        self.db = db

    def save_analysis(self, user_id, analysis_data):
        """
        Saves the decision engine result to the user's history collection.
        """
        if Config.OFFLINE_MODE or not self.db:
            print(f"[Mock DB] Saved analysis for user {user_id}")
            return "mock_id_123"

        try:
            # Create a reference to the user's history collection
            doc_ref = self.db.collection('users').document(user_id).collection('history').document()
            
            # Add metadata
            data_to_save = {
                **analysis_data,
                "created_at": datetime.datetime.now().isoformat(),
                "user_id": user_id
            }
            
            doc_ref.set(data_to_save)
            return doc_ref.id
        except Exception as e:
            print(f"Firestore Write Error: {e}")
            return None