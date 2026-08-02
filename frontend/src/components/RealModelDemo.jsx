// SafeSwipe/frontend/src/components/RealModelDemo.jsx

import { useEffect, useState } from "react";
import { getSamples, predictSample } from "../api/backend";

function RealModelDemo() {
  const [samples, setSamples] = useState([]);
  const [results, setResults] = useState({});

  useEffect(() => {
    getSamples().then(setSamples);
  }, []);

  async function handleCheck(sampleId) {
    const result = await predictSample(sampleId);
    setResults((prev) => ({ ...prev, [sampleId]: result }));
  }

  return (
    <div>
      <h2>Try a Real Transaction</h2>
      <p>
        These are real transactions from the dataset used to train the model
        (not made up). Click one to see the model's live prediction compared
        to the actual outcome.
      </p>
      <ul>
        {samples.map((s) => {
          const result = results[s.sample_id];
          return (
            <li key={s.sample_id}>
              Sample #{s.sample_id} — Amount: ${s.amount}{" "}
              <button onClick={() => handleCheck(s.sample_id)}>Check</button>
              {result && (
                <span>
                  {" "}
                  — Model says:{" "}
                  {result.predicted_fraud ? "FRAUD" : "Not Fraud"} (
                  {(result.fraud_probability * 100).toFixed(1)}% confidence) |
                  Actual: {result.actual_label === 1 ? "FRAUD" : "Not Fraud"}
                </span>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default RealModelDemo;