class IrrigationAdvisor:
    def analyze(self, crop_data: dict, weather: dict) -> dict:
        soil_type = crop_data.get('soil_type', 'Loam').lower()
        temp = weather.get('temp', 25)
        humidity = weather.get('humidity', 50)
        
        needs_water = False
        reason = "Soil moisture adequate."
        
        # Simple evapotranspiration logic
        if temp > 30 and humidity < 40:
            needs_water = True
            reason = "High evaporation rate detected."
        elif soil_type == 'sandy' and temp > 25:
            needs_water = True
            reason = "Sandy soil retains less water."

        return {
            "action": "Irrigate" if needs_water else "Hold",
            "quantity_liters_per_sqm": 6 if needs_water else 0,
            "reason": reason,
            "method": "Drip" if soil_type == 'sandy' else "Sprinkler"
        }