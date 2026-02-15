import { useState } from "react";
import api from "../api/client";
import type { DecisionRequest, DecisionResponse } from "../types/api";

interface Props {
  onResult: (d: DecisionResponse) => void;
}

export default function DecisionForm({ onResult }: Props) {
  const [form, setForm] = useState<DecisionRequest>({
    crop: "",
    location: "",
    sowing_date: "",
  });

  const submit = async () => {
    const res = await api.post<DecisionResponse>("/decision", form);
    onResult(res.data);
  };

  return (
    <div>
      <h3>Daily Decision</h3>
      <input placeholder="Crop" onChange={e => setForm({ ...form, crop: e.target.value })} />
      <input placeholder="Location" onChange={e => setForm({ ...form, location: e.target.value })} />
      <input type="date" onChange={e => setForm({ ...form, sowing_date: e.target.value })} />
      <button onClick={submit}>Submit</button>
    </div>
  );
}
