# SIGMA

**Sistema Integrado Georreferenciado de Monitoramento de Anemômetros**

Base inicial do projeto de monitoramento remoto de sensores meteorológicos.
A estrutura segue uma organização Django inspirada nos projetos PycodeBR:
`core` para configuração, apps de domínio na raiz, separação de domínio,
repositories, services e API, além de documentação e comandos de gerenciamento.

## Stack

- Python 3.11+
- Django 5.2+
- Django REST Framework
- PostgreSQL
- MQTT via `paho-mqtt`
- React 19 + TypeScript + Vite
- `uv` para dependências Python
- `pnpm` para o frontend
- Docker Compose para aplicação, worker MQTT e banco

## Estrutura

```text
sigma/
├── core/                         # Configuração, URLs e WSGI/ASGI
├── telemetry/                   # Domínio de dispositivos e leituras
│   ├── api/                      # Serializers, views e URLs REST
│   ├── domain/                   # Parsing e regras independentes de Django
│   ├── repositories/             # Persistência
│   ├── services/                 # Casos de uso
│   ├── management/commands/      # Worker MQTT
│   └── tests/
├── frontend/                    # React/Vite
├── templates/                   # Templates Django
├── static/                      # Assets Django
├── docs/                        # Decisões e arquitetura
├── compose.yaml
├── Dockerfile
├── pyproject.toml
└── uv.lock
```

## Setup local

### Backend

```bash
uv sync
copy .env.example .env  # Windows
uv run python manage.py migrate
uv run python manage.py runserver
```

A página placeholder fica em `http://127.0.0.1:8000/`.

Endpoints iniciais:

- `GET /api/health/`
- `GET /api/devices/`
- `GET /api/telemetry/`

### Frontend

```bash
cd frontend
pnpm install
pnpm dev
```

A interface React fica em `http://127.0.0.1:5173/` e usa proxy local para a API
Django em `http://127.0.0.1:8000/`.

### Testes e qualidade

```bash
uv run pytest -q
uv run ruff check .
cd frontend && pnpm build
```

## Docker Compose

```bash
docker compose up --build
```

Os serviços são:

- `web`: Django/DRF;
- `mqtt-worker`: assinatura do tópico e persistência das leituras;
- `db`: PostgreSQL com volume local.

O worker usa as variáveis `MQTT_HOST`, `MQTT_PORT`, `MQTT_TOPIC` e credenciais
opcionais. O payload bruto é preservado; os três valores ainda sem semântica
confirmada ficam como `value_1`, `value_2` e `value_3`.

## Fluxo MQTT inicial

```text
ESP32 → test.mosquitto.org → mqtt-worker → PostgreSQL → Django API → React
```

O cadastro visual de dispositivos não faz parte desta primeira etapa. O worker
cria o registro inicial do dispositivo ao receber uma leitura válida.
