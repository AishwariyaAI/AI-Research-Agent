import { useState } from "react";
import API from "../api/api";

function ChatBot() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);

  const send = async () => {
    const res = await API.post("/api/chat", {
      prompt: msg,
    });

    setChat([
      ...chat,
      { role: "user", text: msg },
      { role: "bot", text: res.data.answer },
    ]);

    setMsg("");
  };

  return (
    <div>
      <h2>Ask AI</h2>

      {chat.map((c, i) => (
        <p key={i}>
          <b>{c.role}:</b> {c.text}
        </p>
      ))}

      <input
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        placeholder="Ask about your resume..."
      />

      <button onClick={send}>Send</button>
    </div>
  );
}

export default ChatBot;