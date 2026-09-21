# Arquitetura inicial

SIGMA segue uma organização Django inspirada nos projetos PycodeBR: pacote `core` para configuração, apps de domínio na raiz, `templates`, `static`, `utils` e comandos de gerenciamento. A lógica de ingestão MQTT fica separada em domínio, repositories e services para manter o worker pequeno e testável.

```text
ESP32 -> MQTT broker -> telemetry management command -> PostgreSQL -> Django API -> React
```

## Componentes

- `core/`: settings, URLs e ponto de entrada Django.
- `telemetry/`: domínio de dispositivos e leituras.
- `telemetry/domain/`: parsing e regras independentes de infraestrutura.
- `telemetry/repositories/`: persistência Django.
- `telemetry/services/`: casos de uso de ingestão.
- `telemetry/api/`: serializers, views e URLs REST.
- `frontend/`: SPA React/Vite.
- `compose.yaml`: web, worker MQTT e PostgreSQL.
