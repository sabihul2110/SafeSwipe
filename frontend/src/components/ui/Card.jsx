// SafeSwipe/frontend/src/components/ui/Card.jsx

function Card({ children }) {
  return (
    <div
      style={{
        background: "var(--color-surface)",
        borderRadius: "var(--radius-md)",
        padding: "var(--spacing-lg)",
        marginBottom: "var(--spacing-md)",
      }}
    >
      {children}
    </div>
  );
}

export default Card;