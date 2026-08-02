// SafeSwipe/frontend/src/components/TransactionHistory.jsx

import { useEffect, useState } from "react";
import { getTransactionHistory } from "../api/backend";

function TransactionHistory({ refreshTrigger }) {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    getTransactionHistory().then(setTransactions);
  }, [refreshTrigger]);

  return (
    <div>
      <h2>Transaction History</h2>
      {transactions.length === 0 && <p>No transactions yet.</p>}
      <ul>
        {transactions.map((t) => (
          <li key={t.id}>
            {t.merchant} — ${t.amount} —{" "}
            {t.is_fraud ? "FRAUD" : "OK"} ({t.reason})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TransactionHistory;