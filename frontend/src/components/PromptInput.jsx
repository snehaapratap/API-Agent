import { useState } from "react";
import axios from "axios";

const PromptInput = ({ setResponse }) => {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt) return;

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/generate", {
        prompt,
      });
      setResponse(res.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="container">
      <form onSubmit={handleSubmit} className="form">
        <input
          type="text"
          placeholder="Enter your query..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="input"
        />
        <button type="submit" className="button">
          Generate API
        </button>
      </form>
    </div>
  );
};

export default PromptInput;
