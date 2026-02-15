import random

class SensorService:
    def get_readings(self):
        return {
            "soil_moisture": round(random.uniform(45, 75), 1), # %
            "nitrogen": round(random.uniform(120, 160), 0), # kg/ha
            "phosphorus": round(random.uniform(30, 50), 0),
            "potassium": round(random.uniform(100, 150), 0),
            "uv_index": round(random.uniform(3, 8), 1),
            "battery": 85,
            "signal": "Strong"
        }