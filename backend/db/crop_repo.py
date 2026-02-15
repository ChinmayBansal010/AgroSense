
from firebase.firebase_init import db

def get_crop_stage(crop: str, days_since: int):
    docs = db.collection("crop_calendar").where("crop", "==", crop).order_by("max_days").stream()
    for doc in docs:
        d = doc.to_dict()
        if days_since <= d["max_days"]:
            return d["stage"]
    return "Unknown"
