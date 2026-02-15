import type { DecisionResponse } from "../types/api";
import "../styles/card.css";

interface Props {
  data: DecisionResponse;
}

export default function DecisionCard({ data }: Props) {
  return (
    <div className="card">
      <h3>Today’s Recommendation</h3>

      <p><b>Crop Stage:</b> {data.stage}</p>
      <p><b>Risk Level:</b> {data.risk_assessment.level}</p>

      <ul>
        <li>💧 {data.recommendations.irrigation}</li>
        <li>🐛 {data.recommendations.pest}</li>
        <li>🌾 {data.recommendations.harvest}</li>
      </ul>
    </div>
  );
}
