
from fastapi import FastAPI, Depends
from core.schemas import DecisionRequest, MarketUpdateRequest
from firebase.auth_middleware import firebase_auth, admin_only
from engine.decision_engine import generate_decision
from db.firestore_repo import save_decision, get_history
from db.market_repo import add_market_price

app = FastAPI(title="AgroSense API", version="1.4")

@app.post("/decision")
def decision(data: DecisionRequest, user=Depends(firebase_auth)):
    result = generate_decision(data)
    save_decision(user["uid"], result)
    return result

@app.get("/history")
def history(user=Depends(firebase_auth)):
    return get_history(user["uid"])

@app.post("/admin/market/update")
def update_market(data: MarketUpdateRequest, user=Depends(firebase_auth)):
    admin_only(user)
    add_market_price(data.crop, data.price)
    return {"status": "updated"}

@app.get("/alerts")
def get_alerts(user=Depends(firebase_auth)):
    history = get_history(user["uid"])
    alerts = []
    for record in history:
        # If rainfall predicted > 50mm in last record, trigger alert
        if record.get("weather", {}).get("rainfall", 0) > 50:
            alerts.append({
                "type": "Flood Warning",
                "crop": record["crop"],
                "message": f"Heavy rain detected in {record['location']}. Postpone irrigation."
            })
    return alerts