import { useState } from "react";
import import API from "../api/api";

function UploadResume({ onUpload }) {
  const [file, setFile] = useState(null);

  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      await API.post("/api/upload-resume", formData);
      alert("Resume uploaded successfully!");
      onUpload(true);
    } catch (err) {
      alert("Upload failed");
    }
  };

  return (
    <div className="upload">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadFile}>Upload Resume</button>
    </div>
  );
}

export default UploadResume;