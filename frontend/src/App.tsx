import { useEffect, useState } from "react";

type Health = { status: string; service: string };

export default function App() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/health/")
      .then((response) => {
        if (!response.ok) throw new Error(`API respondeu ${response.status}`);
        return response.json() as Promise<Health>;
      })
      .then(setHealth)
      .catch((reason: Error) => setError(reason.message));
  }, []);

  return (
    <main className="shell">
      <section className="card">
        <span className="eyebrow">SIGMA · placeholder</span>
        <h1>Monitoramento georreferenciado de anemômetros</h1>
        <p className="lead">
          Estrutura inicial React + Django preparada para receber as leituras MQTT.
        </p>
        <div className={`status ${health ? "ok" : error ? "error" : "loading"}`}>
          {health ? `API online · ${health.service}` : error ? `API indisponível · ${error}` : "Consultando API…"}
        </div>
      </section>
    </main>
  );
}
