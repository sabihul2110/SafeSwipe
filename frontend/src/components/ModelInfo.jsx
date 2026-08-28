// SafeSwipe/frontend/src/components/ModelInfo.jsx

import { useEffect, useState } from "react";
import { getModelInfo } from "../api/backend";
import Card from "./ui/Card";

function ModelInfo() {
  const [info, setInfo] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    getModelInfo()
      .then(setInfo)
      .catch(() => setError("Couldn't load model info. Is the backend running?"));
  }, []);

  if (error) {
    return <p style={{ color: "var(--color-danger)" }}>{error}</p>;
  }

  if (!info) {
    return null;
  }

  return (
    <Card>
      <p style={{ margin: 0 }}>
        <strong>{info.model_name}</strong>
      </p>
      <p style={{ color: "var(--color-text-muted)", marginTop: "var(--spacing-sm)" }}>
        Threshold: {info.threshold} &nbsp;|&nbsp; Precision: {info.precision} &nbsp;|&nbsp;
        Recall: {info.recall} &nbsp;|&nbsp; F1: {info.f1_score}
      </p>
      <p style={{ color: "var(--color-text-muted)", marginTop: "var(--spacing-sm)" }}>
        {info.threshold_reasoning}
      </p>
    </Card>
  );
}

export default ModelInfo;
