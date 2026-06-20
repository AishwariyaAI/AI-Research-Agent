import { useState } from "react";
import API from "../api/api";

export default function Ats() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const analyze = async () => {
    const res = await API.post("/api/ats-score", { text });
    setResult(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>ATS Score Checker</h2>

      <textarea
        rows="8"
        style={{ width: "100%" }}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste resume text..."
      />

      <button onClick={analyze}>Analyze</button>

      {result && (
        <div>
          <h3>Score: {result.score}</h3>
          <p>Found: {result.found_skills.join(", ")}</p>
          <p>Missing: {result.missing_skills.join(", ")}</p>
        </div>
      )}
    </div>
  );
}