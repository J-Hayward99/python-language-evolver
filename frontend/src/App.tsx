import { useEffect, useState } from "react";

type HealthResponse = {
  status: string;
};

function App() {
  const [status, setStatus] = useState<string>("loading...");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/health")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json() as Promise<HealthResponse>;
      })
      .then((data) => setStatus(data.status))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Health check</h1>
      {error ? <p>Error: {error}</p> : <p>Backend says: {status}</p>}
    </div>
  );
}

export default App;