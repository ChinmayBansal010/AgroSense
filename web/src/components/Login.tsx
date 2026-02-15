import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../auth/firebase";
import { attachToken } from "../api/client";
import { useState } from "react";

interface Props {
  onSuccess: () => void;
}

export default function Login({ onSuccess }: Props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleLogin = async () => {
    try {
      const cred = await signInWithEmailAndPassword(auth, email, password);
      const token = await cred.user.getIdToken(true);
      attachToken(token);
      onSuccess();
    } catch (err) {
      setError("Login failed");
    }
  };

  return (
    <div>
      <h2>AgroSense Login</h2>
      <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
      {error && <p>{error}</p>}
    </div>
  );
}
