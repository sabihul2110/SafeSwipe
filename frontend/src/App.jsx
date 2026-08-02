// SafeSwipe/frontend/src/App.jsx

import { useState } from "react";
import TransactionForm from "./components/TransactionForm";
import TransactionHistory from "./components/TransactionHistory";
import RealModelDemo from "./components/RealModelDemo";

function App() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  return (
    <div>
      <h1>SafeSwipe</h1>

      <section>
        <h2>Real ML Model Demo</h2>
        <RealModelDemo />
      </section>

      <hr />

      <section>
        <h2>Simple Rule-Based Demo</h2>
        <p>
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