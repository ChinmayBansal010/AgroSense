import datetime

class HarvestAnalyzer:
    def analyze(self, crop_data: dict, weather: dict) -> dict:
        planting_date_str = crop_data.get('planting_date')
        if not planting_date_str:
            return {"estimated_date": "Unknown", "days_remaining": 0}

        try:
            planting_date = datetime.datetime.fromisoformat(planting_date_str)
            # Simple assumption: 120 day crop cycle
            harvest_date = planting_date + datetime.timedelta(days=120)
            days_remaining = (harvest_date - datetime.datetime.now()).days
            
            return {
                "estimated_date": harvest_date.strftime("%Y-%m-%d"),
                "days_remaining": max(0, days_remaining),
                "readiness": "Ready" if days_remaining <= 0 else "Growing"
            }
        except:
            return {"estimated_date": "Error", "days_remaining": 0}