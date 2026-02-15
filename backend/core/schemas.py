
from pydantic import BaseModel
from datetime import date

class DecisionRequest(BaseModel):
    crop: str
    location: str
    sowing_date: date

class MarketUpdateRequest(BaseModel):
    crop: str
    price: float
