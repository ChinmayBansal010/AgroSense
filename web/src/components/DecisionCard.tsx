import type { DecisionResponse } from "../types/api";
import { CloudRain, Thermometer, TrendingUp, Droplets, AlertTriangle } from "lucide-react";

export default function DecisionCard({ data }: { data: DecisionResponse }) {
  const getRiskColor = (level: string) => {
    if (level === "High") return "text-red-600 bg-red-50 border-red-100";
    if (level === "Medium") return "text-yellow-600 bg-yellow-50 border-yellow-100";
    return "text-green-600 bg-green-50 border-green-100";
  };

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="bg-green-600 px-6 py-4 flex justify-between items-center text-white">
        <h3 className="text-lg font-semibold">{data.crop} Analysis - {data.location}</h3>
        <span className="text-sm font-medium opacity-90">Stage: {data.stage}</span>
      </div>
      
      <div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className={`p-4 rounded-xl border ${getRiskColor(data.risk_assessment.level)}`}>
          <div className="flex items-center gap-2 mb-2 font-bold">
            <AlertTriangle size={20} /> AI Risk Level
          </div>
          <div className="text-2xl font-black">{data.risk_assessment.level}</div>
          <div className="text-xs mt-1 opacity-80">Score: {data.risk_assessment.score}</div>
        </div>

        <div className="p-4 rounded-xl bg-blue-50 border border-blue-100 text-blue-700">
          <div className="flex items-center gap-2 mb-2 font-bold">
            <Droplets size={20} /> Irrigation
          </div>
          <p className="text-sm">{data.recommendations.irrigation}</p>
        </div>

        <div className="p-4 rounded-xl bg-purple-50 border border-purple-100 text-purple-700">
          <div className="flex items-center gap-2 mb-2 font-bold">
            <TrendingUp size={20} /> Market Signal
          </div>
          <p className="text-sm">{data.recommendations.harvest}</p>
        </div>
      </div>

      <div className="px-6 py-4 bg-gray-50 border-t border-gray-100 flex gap-8">
        <div className="flex items-center gap-2 text-gray-600">
          <Thermometer size={18} />
          <span className="text-sm font-medium">{data.weather.temperature}°C</span>
        </div>
        <div className="flex items-center gap-2 text-gray-600">
          <CloudRain size={18} />
          <span className="text-sm font-medium">{data.weather.rainfall}mm Rain</span>
        </div>
      </div>
    </div>
  );
}