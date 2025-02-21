const ResponseDisplay = ({ response }) => {
  return (
    <div className="response-box">
      <h2>Generated API Response</h2>
      <pre>{JSON.stringify(response, null, 2)}</pre>
    </div>
  );
};

export default ResponseDisplay;
