// SafeSwipe/frontend/src/components/TransactionForm.jsx

import { useState } from "react";
import { checkTransaction } from "../api/backend";
import Card from "./ui/Card";
import Button from "./ui/Button";
import Badge from "./ui/Badge";

function TransactionForm({ onChecked }) {
  const [amount, setAmount] = useState("");
  const [merchant, setMerchant] = useState("");
  const [result, setResult] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    const data = await checkTransaction(Number(amount), merchant);
    setResult(data);
    onChecked();
  }

  const inputStyle = {
    display: "block",
    marginBottom: "var(--spacing-sm)",
    padding: "8px",
    borderRadius: "var(--radius-md)",
    border: "1px solid var(--color-text-muted)",
    background: "var(--color-bg)",
    color: "var(--color-text)",
    width: "100%",
  };

  return (
    <Card>
      <form onSubmit={handleSubmit}>
        <label>Amount</label>
        <input
          style={inputStyle}
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          required
        />
        <label>Merchant</label>
        <input
          style={inputStyle}
          type="text"
          value={merchant}
          onChange={(e) => setMerchant(e.target.value)}
          required
        />
        <Button type="submit">Check</Button>
      </form>

      {result && (
        <div style={{ marginTop: "var(--spacing-sm)" }}>
          <Badge isFraud={result.is_fraud} /> — {result.reason}
        </div>
      )}
    </Card>
  );
}

export default TransactionForm;