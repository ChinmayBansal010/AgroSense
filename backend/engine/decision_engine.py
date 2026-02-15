
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
    weather = fetch_weather(data.location)
    days_since = (date.today() - data.sowing_date).days
    stage = get_crop_stage(data.crop, days_since)
    market = get_market_signal(data.crop)

    risk_score = compute_risk_score(weather["rainfall"], weather["humidity"], weather["temperature"])

    return {
        "crop": data.crop,
        "location": data.location,
        "days_since_sowing": days_since,
        "stage": stage,
        "weather": weather,
        "risk_assessment": {
            "score": risk_score,
            "level": risk_label(risk_score)
        },
        "recommendations": {
            "irrigation": irrigation(stage, weather["rainfall"]),
            "pest": pest_risk(weather["temperature"], weather["humidity"]),
            "harvest": harvest(stage, market)
        }
    }
