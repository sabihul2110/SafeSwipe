// SafeSwipe/frontend/src/App.jsx

import { useState } from "react";
import TransactionForm from "./components/TransactionForm";
import TransactionHistory from "./components/TransactionHistory";

function App() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  return (
    <div>
      <h1>SafeSwipe</h1>
      <TransactionForm onChecked={() => setRefreshTrigger((n) => n + 1)} />
      <TransactionHistory refreshTrigger={refreshTrigger} />
    </div>
  );
}

export default App;