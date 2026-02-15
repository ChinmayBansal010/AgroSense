export interface DecisionRequest {
  crop: string;
  location: string;
  sowing_date: string;
}

export interface RiskAssessment {
  score: number;
  level: "Low" | "Medium" | "High";
}

export interface DecisionResponse {
  crop: string;
  location: string;
  stage: string;
  days_since_sowing: number;
  weather: {
    rainfall: number;
    temperature: number;
    humidity: number;
  };
  risk_assessment: RiskAssessment;
  recommendations: {
    irrigation: string;
    pest: string;
    harvest: string;
  };
}
