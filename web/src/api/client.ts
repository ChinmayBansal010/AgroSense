import axios from "axios";
import { auth } from "../auth/firebase";

const API_URL = import.meta.env.VITE_BACKEND_URL || "http://127.0.0.1:5000";

export const client = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Automatic Token Injection
client.interceptors.request.use(async (config) => {
  const user = auth.currentUser;
  if (user) {
    const token = await user.getIdToken();
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});