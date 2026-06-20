import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ display: "flex", gap: "15px", padding: "10px" }}>
      <Link to="/">Home</Link>
      <Link to="/chat">Chat</Link>
      <Link to="/resume">Resume</Link>
      <Link to="/roadmap">Roadmap</Link>
      <Link to="/skill-gap">Skill Gap</Link>
    </nav>
  );
}