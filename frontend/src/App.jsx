import { useState } from "react";
import PromptInput from "./components/PromptInput";
import ResponseDisplay from "./components/ResponseDisplay";
import "./styles.css";

function App() {
  const [response, setResponse] = useState(null);

  return (
    <div className="app">
      <h1>Graph RAG API Assistant</h1>
      <PromptInput setResponse={setResponse} />
      {response && <ResponseDisplay response={response} />}
    </div>
  );
}

export default App;
