from .irrigation import IrrigationAdvisor
from .pest import PestControl
from .harvest import HarvestAnalyzer
from ml.risk_model import RiskModel
from services.weather_service import WeatherService
import datetime

class DecisionEngine:
    def __init__(self):
        self.irrigation = IrrigationAdvisor()
        self.pest = PestControl()
        self.harvest = HarvestAnalyzer()
        self.risk_model = RiskModel()
        self.weather_service = WeatherService()

    def analyze(self, data: dict) -> dict:
        try:
            # 1. Fetch Context
            city = data.get('location', 'Unknown')
            weather_context = self.weather_service.get_current_weather(city)

            # 2. Run Modules
            irrigation_plan = self.irrigation.analyze(data, weather_context)
            pest_report = self.pest.analyze(data, weather_context)
            harvest_plan = self.harvest.analyze(data, weather_context)

            # 3. Run AI Models
            risk_assessment = self.risk_model.predict_risk(data, weather_context)
            yield_forecast = self.risk_model.predict_yield(data, risk_assessment['score'])

            return {
                "summary": self._generate_summary(risk_assessment, weather_context),
                "risk_analysis": risk_assessment,
                "yield_forecast": yield_forecast,
                "irrigation": irrigation_plan,
                "pest_control": pest_report,
                "harvest": harvest_plan,
                "weather_context": weather_context,
                "timestamp": datetime.datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}

    def _generate_summary(self, risk, weather):
        status = "Simulation" if weather.get('is_mock') else "Live"
        msg = f"[{status}] {weather['city']}: {weather['condition']}."
        
        if risk['level'] == 'Critical':
            msg += " CRITICAL ALERT: Immediate intervention needed."
        elif risk['level'] == 'High':
            msg += " WARNING: High risk factors detected."
        else:
            msg += " Conditions optimal."
        return msg