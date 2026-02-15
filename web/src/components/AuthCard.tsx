import { useState } from "react";
import { auth } from "../auth/firebase";
import {
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
} from "firebase/auth";
import { attachToken } from "../api/client";
import "../styles/auth.css";

interface Props {
  onAuth: () => void;
}

export default function AuthCard({ onAuth }: Props) {
  const [isSignup, setIsSignup] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const submit = async () => {
    try {
      const cred = isSignup
        ? await createUserWithEmailAndPassword(auth, email, password)
        : await signInWithEmailAndPassword(auth, email, password);

      const token = await cred.user.getIdToken(true);
      attachToken(token);
      onAuth();
    } catch {
      setError("Authentication failed");
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>AgroSense</h2>
        <p>{isSignup ? "Create an account" : "Welcome back"}</p>

        <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
        <input
          type="password"
          placeholder="Password"
          onChange={e => setPassword(e.target.value)}
        />

        {error && <span className="error">{error}</span>}

        <button onClick={submit}>
          {isSignup ? "Sign Up" : "Sign In"}
        </button>

        <span className="toggle" onClick={() => setIsSignup(!isSignup)}>
          {isSignup ? "Already have an account?" : "New user? Sign up"}
        </span>
      </div>
    </div>
  );
}
