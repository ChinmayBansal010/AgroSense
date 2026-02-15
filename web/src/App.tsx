import { useState } from "react";
import AuthCard from "./components/AuthCard";
import Dashboard from "./pages/Dashboard";

export default function App() {
  const [authed, setAuthed] = useState(false);
  return authed ? <Dashboard /> : <AuthCard onAuth={() => setAuthed(true)} />;
}
