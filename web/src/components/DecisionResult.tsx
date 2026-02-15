import type { DecisionResponse } from "../types/api";

interface Props {
  data: DecisionResponse | null;
}

export default function DecisionResult({ data }: Props) {
  if (!data) return null;

  return (
    <div>
      <h3>Recommendation</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
