import { useState } from "react";
import DecisionForm from "../components/DecisionForm";
import DecisionCard from "../components/DecisionCard";
import HistoryList from "../components/HistoryList";
import Header from "../components/Header";
import type { DecisionResponse } from "../types/api";
import "../styles/dashboard.css";

export default function Dashboard() {
  const [decision, setDecision] = useState<DecisionResponse | null>(null);

  return (
    <>
      <Header />
      <div className="dashboard">
        <DecisionForm onResult={setDecision} />
        {decision && <DecisionCard data={decision} />}
        <HistoryList />
      </div>
    </>
  );
}
