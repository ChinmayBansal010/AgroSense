import { useState } from "react";
import DecisionForm from "../components/DecisionForm";
import DecisionCard from "../components/DecisionCard";
import HistoryList from "../components/HistoryList";
import Header from "../components/Header";
import type { DecisionResponse } from "../types/api";

export default function Dashboard() {
  const [decision, setDecision] = useState<DecisionResponse | null>(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-slate-50">
      <Header />
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-1">
            <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
              <h2 className="text-xl font-bold text-slate-800 mb-6">Field Parameters</h2>
              <DecisionForm onResult={(res) => { setDecision(res); setLoading(false); }} />
            </div>
          </div>
          <div className="lg:col-span-2 space-y-6">
            {decision && <DecisionCard data={decision} />}
            <HistoryList />
          </div>
        </div>
      </main>
    </div>
  );
}