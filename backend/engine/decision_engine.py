
from datetime import date
from services.weather_service import fetch_weather
from db.crop_repo import get_crop_stage
from db.market_repo import get_market_signal
from engine.irrigation import irrigation
from engine.pest import pest_risk
from engine.harvest import harvest
from ml.risk_model import compute_risk_score
from ml.risk_utils import risk_label

def generate_decision(data):
    # Existing logic
    weather = fetch_weather(data.location)
    days_since = (date.today() - data.sowing_date).days
    
    # NEW: Advanced ML-driven features
    yield_prediction = compute_yield_estimate(data.crop, days_since, weather)
    market_volatility = calculate_price_risk(data.crop)
    soil_health_score = predict_soil_depletion(days_since)

    return {
        "crop": data.crop,
        "location": data.location,
        "days_since_sowing": days_since,
        "stage": get_crop_stage(data.crop, days_since),
        "weather": weather,
        "analytics": {
            "predicted_yield": f"{yield_prediction} tons/acre",
            "market_trend": "Bullish" if market_volatility > 0.5 else "Stable",
            "soil_depletion_index": soil_health_score
        },
        "risk_assessment": {
            "score": compute_risk_score(weather["rainfall"], weather["humidity"], weather["temperature"]),
            "level": risk_label(compute_risk_score(...))
        },
        "recommendations": {
            "irrigation": irrigation(stage, weather["rainfall"]),
            "pest": "High Risk: Apply Neem-based pesticide" if weather["humidity"] > 80 else "Normal",
            "fertilizer": "Apply NPK 10-10-10" if days_since in [30, 60] else "Maintain soil moisture"
        }
    }