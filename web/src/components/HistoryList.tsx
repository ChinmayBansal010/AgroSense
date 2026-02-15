import { useEffect, useState } from "react";
import api from "../api/client";
import type { DecisionResponse } from "../types/api";
import { Clock, Calendar } from "lucide-react";

export default function HistoryList() {
  const [items, setItems] = useState<DecisionResponse[]>([]);

  useEffect(() => {
    api.get<DecisionResponse[]>("/history").then(r => setItems(r.data));
  }, []);

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
      <div className="flex items-center gap-2 mb-6">
        <Clock className="text-green-600" />
        <h3 className="text-lg font-bold">Activity Log</h3>
      </div>
      <div className="space-y-4">
        {items.map((i, idx) => (
          <div key={idx} className="flex justify-between items-center p-4 rounded-xl bg-slate-50 border border-slate-100">
            <div>
              <p className="font-semibold text-slate-800">{i.crop}</p>
              <p className="text-sm text-slate-500">{i.location}</p>
            </div>
            <div className="text-right">
              <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                i.risk_assessment.level === 'High' ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'
              }`}>
                {i.risk_assessment.level} Risk
              </span>
              <p className="text-xs text-slate-400 mt-1">{i.stage}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}