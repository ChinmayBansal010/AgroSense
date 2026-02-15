export interface DecisionResponse {
  summary: string;
  risk_analysis: {
    score: number;
    level: string;
    factors: string[];
  };
  yield_forecast: {
    predicted_yield: number;
    unit: string;
    confidence: string;
  };
  irrigation: {
    action: string;
    reason: string;
    quantity_liters_per_sqm: number;
    method: string;
  };
  pest_control: {
    risk_level: string;
    potential_pests: string[];
    preventative_action: string;
  };
  harvest: {
    estimated_date: string;
    days_remaining: number;
    readiness: string;
  };
  weather_context: {
    city: string;
    temp: number;
    humidity: number;
    condition: string;
    description: string;
    wind_speed: number;
    is_mock: boolean;
  };
  timestamp: string;
  db_id?: string;
}

export interface DecisionFormData {
  crop_name: string;
  location: string;
  area_size: number;
  soil_type: string;
  planting_date: string;
}

export interface MarketData {
  market_status: string;
  last_updated: string;
  commodities: {
    name: string;
    price: number;
    unit: string;
    change: number;
    trend: "up" | "down";
  }[];
}

export interface SensorData {
  soil_moisture: number;
  nitrogen: number;
  phosphorus: number;
  potassium: number;
  uv_index: number;
  battery: number;
  signal: string;
}