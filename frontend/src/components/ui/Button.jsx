// SafeSwipe/frontend/src/components/ui/Button.jsx

function Button({ children, onClick, variant = "primary", type = "button" }) {
  const styles = {
    primary: { background: "var(--color-primary)", color: "#fff" },
    danger: { background: "var(--color-danger)", color: "#fff" },
    success: { background: "var(--color-success)", color: "#fff" },
  };

  return (
    <button
      type={type}
      onClick={onClick}
      style={{
        ...styles[variant],
        border: "none",
        borderRadius: "var(--radius-md)",
        padding: "8px 16px",
        cursor: "pointer",
        fontFamily: "var(--font-family)",
      }}
    >
      {children}
    </button>
  );
}

export default Button;