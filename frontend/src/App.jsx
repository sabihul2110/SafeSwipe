// SafeSwipe/frontend/src/App.jsx

import { useState } from "react";
import TransactionForm from "./components/TransactionForm";
import TransactionHistory from "./components/TransactionHistory";
import RealModelDemo from "./components/RealModelDemo";
import ModelInfo from "./components/ModelInfo";
import Header from "./components/ui/Header";

function App() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  return (
    <div style={{ maxWidth: "700px", margin: "0 auto", padding: "var(--spacing-lg)" }}>
      <Header />

      <section style={{ marginBottom: "var(--spacing-lg)" }}>
        <h2>Real ML Model Demo</h2>
        <p style={{ color: "var(--color-text-muted)" }}>
          This is the actual trained model (Random Forest), tested against
          real transactions from the dataset.
        </p>
        <RealModelDemo />
      </section>

      <section style={{ marginBottom: "var(--spacing-lg)" }}>
        <h2>Model Health</h2>
        <ModelInfo />
      </section>

      <hr style={{ borderColor: "var(--color-surface)" }} />

      <section style={{ marginTop: "var(--spacing-lg)" }}>
        <h2>Simple Rule-Based Demo</h2>
        <p style={{ color: "var(--color-text-muted)" }}>
          This form uses a basic placeholder rule (not the trained model) —
          kept for a quick interactive example.
        </p>
        <TransactionForm onChecked={() => setRefreshTrigger((n) => n + 1)} />
        <TransactionHistory refreshTrigger={refreshTrigger} />
      </section>
    </div>
  );
}

export default App;