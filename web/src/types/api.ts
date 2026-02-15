export interface DecisionRequest {
  crop: string;
  location: string;
  sowing_date: string;
}

export interface DecisionResponse {
  crop: string;
  location: string;
  days_since_sowing: number;
  stage: string;
  weather: {
    rainfall: number;
    temperature: number;
    humidity: number;
  };
  risk_assessment: {
    score: number;
    level: "Low" | "Medium" | "High";
  };
  recommendations: {
    irrigation: string;
    pest: string;
    harvest: string;
  };
}
