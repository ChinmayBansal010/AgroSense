
from firebase.firebase_init import db
from datetime import datetime

def save_decision(uid, decision):
    db.collection("users").document(uid).collection("decisions").add({
        **decision,
        "timestamp": datetime.utcnow()
    })

def get_history(uid, limit=10):
    docs = db.collection("users").document(uid).collection("decisions")         .order_by("timestamp", direction="DESCENDING").limit(limit).stream()
    return [d.to_dict() for d in docs]
