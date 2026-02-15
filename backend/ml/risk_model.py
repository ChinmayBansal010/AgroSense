import random

class RiskModel:
    def predict_risk(self, crop_data: dict, weather_data: dict) -> dict:
        base_risk = 10
        factors = []

        temp = weather_data.get('temp', 25)
        humidity = weather_data.get('humidity', 50)
        wind = weather_data.get('wind_speed', 0)
        crop = crop_data.get('crop_name', 'Unknown').lower()

        # Thermal Logic
        if temp > 35:
            base_risk += 30
            factors.append("Extreme Heat Risk")
        elif temp < 10:
            base_risk += 25
            factors.append("Frost Damage Risk")

        # Moisture Logic
        if humidity > 85:
            base_risk += 20
            factors.append("High Fungal Risk")
        elif humidity < 30:
            base_risk += 15
            factors.append("Drought Stress Risk")

        # Cap Risk
        score = min(max(base_risk, 5), 98)
        
        return {
            "score": round(score, 1),
            "level": "Critical" if score > 75 else "High" if score > 50 else "Medium" if score > 25 else "Low",
            "factors": factors
        }

    def predict_yield(self, crop_data: dict, risk_score: float) -> dict:
        area = float(crop_data.get('area_size', 1))
        base_yield = 4.5 # tons/acre
        
        risk_penalty = (risk_score / 100) * 0.5
        final_yield = (base_yield * area) * (1 - risk_penalty)
        
        return {
            "predicted_yield": round(final_yield, 2),
            "unit": "Tons",
            "confidence": "85%"
        }