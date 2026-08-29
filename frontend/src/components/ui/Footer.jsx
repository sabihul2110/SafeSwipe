// SafeSwipe/frontend/src/components/ui/Footer.jsx

function Footer() {
  return (
    <footer
      style={{
        borderTop: "1px solid var(--color-surface)",
        marginTop: "var(--spacing-lg)",
        paddingTop: "var(--spacing-md)",
        color: "var(--color-text-muted)",
        fontSize: "0.9em",
      }}
    >
      SafeSwipe — a student ML project.{" "}
      <a
      
        href="https://github.com/sabihul2110/SafeSwipe"
        target="_blank"
        rel="noopener noreferrer"
        style={{ color: "var(--color-primary)" }}
      >
        View on GitHub
      </a>
    </footer>
  );
}

export default Footer;