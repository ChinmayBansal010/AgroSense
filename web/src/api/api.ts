import { client } from "./client";
import { DecisionFormData, DecisionResponse, MarketData, SensorData } from "../types/api";

export const postDecision = async (data: DecisionFormData): Promise<DecisionResponse> => {
  const response = await client.post<DecisionResponse>("/analyze", data);
  return response.data;
};

export const getHealth = async () => {
  const response = await client.get("/");
  return response.data;
};

// New Fetchers
export const getMarketData = async (): Promise<MarketData> => {
  const response = await client.get<MarketData>("/market");
  return response.data;
};

export const getSensorData = async (): Promise<SensorData> => {
  const response = await client.get<SensorData>("/sensors");
  return response.data;
};