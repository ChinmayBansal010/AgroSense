import random
from datetime import datetime

class MarketService:
    def get_trends(self):
        # Simulated live market data
        commodities = [
            {"name": "Wheat", "price": 2200, "unit": "₹/Qtl"},
            {"name": "Rice (Basmati)", "price": 3800, "unit": "₹/Qtl"},
            {"name": "Corn/Maize", "price": 1950, "unit": "₹/Qtl"},
            {"name": "Potato", "price": 900, "unit": "₹/Qtl"},
            {"name": "Tomato", "price": 1500, "unit": "₹/Qtl"},
            {"name": "Cotton", "price": 6400, "unit": "₹/Qtl"},
            {"name": "Soybean", "price": 4200, "unit": "₹/Qtl"},
            {"name": "Sugarcane", "price": 340, "unit": "₹/Qtl"}
        ]
        
        # Add volatility
        for c in commodities:
            change = random.uniform(-2.5, 2.5)
            c["price"] = int(c["price"] * (1 + (change/100)))
            c["change"] = round(change, 2)
            c["trend"] = "up" if change > 0 else "down"
            
        return {
            "market_status": "Open",
            "last_updated": datetime.now().isoformat(),
            "commodities": commodities
        }