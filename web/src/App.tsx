import { useState, useEffect } from "react";
import AuthCard from "./components/AuthCard";
import Dashboard from "./pages/Dashboard";
import { auth } from "./auth/firebase";
import "./App.css";

export default function App() {
  const [user, setUser] = useState(auth.currentUser);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((u) => {
      setUser(u);
      setLoading(false);
    });
    return unsubscribe;
  }, []);

  if (loading) return <div className="loading-screen">Loading AgroSense...</div>;

  return (
    <div className="app-root">
      {user ? <Dashboard /> : <AuthCard onAuth={() => {}} />}
    </div>
  );
}