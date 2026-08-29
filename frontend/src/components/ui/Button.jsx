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
        transition: "opacity 0.15s ease",
      }}
      onMouseEnter={(e) => (e.currentTarget.style.opacity = "0.85")}
      onMouseLeave={(e) => (e.currentTarget.style.opacity = "1")}
    >
      {children}
    </button>
  );
}

export default Button;