class PestControl:
    def analyze(self, crop_data: dict, weather: dict) -> dict:
        humidity = weather.get('humidity', 50)
        crop = crop_data.get('crop_name', 'Unknown').lower()
        
        risks = []
        if humidity > 80:
            risks.append("Blight")
            risks.append("Mildew")
        
        if crop == 'corn' and weather.get('temp', 0) > 25:
            risks.append("Fall Armyworm")

        return {
            "risk_level": "High" if len(risks) > 1 else "Low",
            "potential_pests": risks if risks else ["None detected"],
            "preventative_action": "Apply Neem Oil" if risks else "Monitor routinely"
        }