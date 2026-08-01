// SafeSwipe/frontend/src/components/TransactionForm.jsx

import { useState } from "react";
import { checkTransaction } from "../api/backend";

function TransactionForm() {
  const [amount, setAmount] = useState("");
  const [merchant, setMerchant] = useState("");
  const [result, setResult] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    const data = await checkTransaction(Number(amount), merchant);
    setResult(data);
  }

  return (
    <div>
      <h2>Check a Transaction</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Amount: </label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Merchant: </label>
          <input
            type="text"
            value={merchant}
            onChange={(e) => setMerchant(e.target.value)}
            required
          />
        </div>
        <button type="submit">Check</button>
      </form>

      {result && (
        <div>
          <p>Fraud: {result.is_fraud ? "Yes" : "No"}</p>
          <p>Reason: {result.reason}</p>
        </div>
      )}
    </div>
  );
}

export default TransactionForm;