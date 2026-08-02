// SafeSwipe/frontend/src/components/ui/Header.jsx

function Header() {
  return (
    <header
      style={{
        borderBottom: "1px solid var(--color-surface)",
        paddingBottom: "var(--spacing-md)",
        marginBottom: "var(--spacing-lg)",
      }}
    >
      <h1 style={{ margin: 0 }}>SafeSwipe</h1>
      <p style={{ color: "var(--color-text-muted)", margin: "4px 0 0 0" }}>
        Credit card fraud detection — student project
      </p>
    </header>
  );
}

export default Header;