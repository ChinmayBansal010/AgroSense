import { signOut } from "firebase/auth";
import { auth } from "../auth/firebase";

export default function Header() {
  return (
    <header className="header">
      <h3>AgroSense</h3>
      <button onClick={() => signOut(auth)}>Logout</button>
    </header>
  );
}
