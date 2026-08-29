// SafeSwipe/frontend/src/components/TransactionHistory.jsx

import { useEffect, useState } from "react";
import { getTransactionHistory, clearTransactionHistory } from "../api/backend";
import { MESSAGES } from "../constants/messages";
import Card from "./ui/Card";
import Badge from "./ui/Badge";
import Button from "./ui/Button";

function TransactionHistory({ refreshTrigger }) {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    getTransactionHistory().then(setTransactions);
  }, [refreshTrigger]);

  async function handleClear() {
    await clearTransactionHistory();
    setTransactions([]);
  }

  return (
    <div>
      {transactions.length > 0 && (
        <div style={{ marginBottom: "var(--spacing-sm)", textAlign: "right" }}>
          <Button variant="danger" onClick={handleClear}>
            Clear History
          </Button>
        </div>
      )}
      {transactions.length === 0 && (
        <p style={{ color: "var(--color-text-muted)" }}>
          {MESSAGES.NO_TRANSACTIONS}
        </p>
      )}
      {transactions.map((t) => (
        <Card key={t.id}>
          {t.merchant} — ${t.amount} — <Badge isFraud={t.is_fraud} /> (
          {t.reason})
        </Card>
      ))}
    </div>
  );
}

export default TransactionHistory;