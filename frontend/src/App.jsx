import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Chat from "./pages/Chat";
import Resume from "./pages/Resume";
import Roadmap from "./pages/Roadmap";
import SkillGap from "./pages/SkillGap";
import Ats from "./pages/Ats";

export default function App() {
  return (
    <div>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/resume" element={<Resume />} />
        <Route path="/roadmap" element={<Roadmap />} />
        <Route path="/skill-gap" element={<SkillGap />} />
        <Route path="/ats" element={<Ats />} />
      </Routes>
    </div>
  );
}