// SafeSwipe/frontend/src/components/ui/Badge.jsx

function Badge({ isFraud }) {
  return (
    <span
      style={{
        background: isFraud ? "var(--color-danger)" : "var(--color-success)",
        color: "#fff",
        borderRadius: "var(--radius-md)",
        padding: "2px 10px",
        fontSize: "0.85em",
        fontWeight: "bold",
      }}
    >
      {isFraud ? "FRAUD" : "OK"}
    </span>
  );
}

export default Badge;