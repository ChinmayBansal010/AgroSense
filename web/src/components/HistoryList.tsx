import { useEffect, useState } from "react";
import api from "../api/client";
import type { DecisionResponse } from "../types/api";
import "../styles/card.css";

export default function HistoryList() {
  const [items, setItems] = useState<DecisionResponse[]>([]);

  useEffect(() => {
    api.get<DecisionResponse[]>("/history").then(r => setItems(r.data));
  }, []);

  return (
    <div className="card">
      <h3>Previous Decisions</h3>
      {items.map((i, idx) => (
        <p key={idx}>
          {i.crop} – {i.stage} – {i.risk_assessment.level}
        </p>
      ))}
    </div>
  );
}
