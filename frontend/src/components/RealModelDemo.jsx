// SafeSwipe/frontend/src/components/RealModelDemo.jsx

import { useEffect, useState } from "react";
import { getSamples, predictSample } from "../api/backend";
import Card from "./ui/Card";
import Button from "./ui/Button";
import Badge from "./ui/Badge";

function RealModelDemo() {
  const [samples, setSamples] = useState([]);
  const [results, setResults] = useState({});
  const [loadingId, setLoadingId] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    getSamples()
      .then(setSamples)
      .catch(() => setError("Couldn't load samples. Is the backend running?"));
  }, []);

  async function handleCheck(sampleId) {
    setLoadingId(sampleId);
    setError(null);
    try {
      const result = await predictSample(sampleId);
      setResults((prev) => ({ ...prev, [sampleId]: result }));
    } catch {
      setError("Prediction failed. Check that the backend is running.");
    }
    setLoadingId(null);
  }

  return (
    <div>
      <p style={{ color: "var(--color-text-muted)" }}>
        These are real transactions from the dataset used to train the model
        (not made up). Click one to see the model's live prediction compared
        to the actual outcome.
      </p>

      {error && <p style={{ color: "var(--color-danger)" }}>{error}</p>}
      
      {samples.map((s) => {
        const result = results[s.sample_id];
        return (
          <Card key={s.sample_id}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
              }}
            >
              <span>
                Sample #{s.sample_id} — Amount: ${s.amount}
              </span>
              <Button onClick={() => handleCheck(s.sample_id)}>
                {loadingId === s.sample_id ? "Checking..." : "Check"}
              </Button>
            </div>
            {result && (
              <div style={{ marginTop: "var(--spacing-sm)" }}>
                Model says: <Badge isFraud={result.predicted_fraud} /> (
                {(result.fraud_probability * 100).toFixed(1)}% confidence)
                {" — "}
                Actual: <Badge isFraud={result.actual_label === 1} />
              </div>
            )}
          </Card>
        );
      })}
    </div>
  );
}

export default RealModelDemo;