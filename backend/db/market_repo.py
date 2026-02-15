
from firebase.firebase_init import db
from datetime import datetime

def get_market_signal(crop: str):
    doc = db.collection("market_prices").document(crop).get()
    if not doc.exists:
        return "HOLD"
    prices = doc.to_dict()["prices"]
    avg = sum(prices)/len(prices)
    latest = prices[-1]
    if latest > avg*1.05: return "SELL"
    if latest < avg*0.95: return "WAIT"
    return "HOLD"

def add_market_price(crop: str, price: float):
    ref = db.collection("market_prices").document(crop)
    doc = ref.get()
    prices = doc.to_dict()["prices"] if doc.exists else []
    prices.append(price)
    ref.set({"prices": prices, "last_updated": datetime.utcnow()})
