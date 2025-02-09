# Self-hosted AI Starter Kit (vom n8n-Team), modifiziert von Felix

**Self-hosted AI Starter Kit** ist ein offenes, Docker Compose Template, das
eine voll ausgestattete lokale AI- und Low-Code-Entwicklungsumgebung schnell einrichtet, einschließlich Open WebUI als Interface zum Chatten mit deinen n8n-Agenten.

Dies ist die Version von Felix mit einigen Verbesserungen sowie der Erweiterung um Open WebUI, Flowise, Elasticsearch, Kibana!
Außerdem wird der lokale RAG AI Agent Workflow aus dem Video automatisch in deiner
n8n-Instanz vorhanden sein, wenn du dieses Setup anstelle der von n8n bereitgestellten Basis verwendest!

Original wurde die Erweiterung mit OpenWebUI und Flowise von Coleam00 auf GitHub veröffentlicht.

Ich werde den Flowchart, bzw. die Tools ständig erweitern, und diese im Toturial mit aufnehmen.

[Original Local AI Starter Kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)

Lade die N8N + Open WebUI Integration [direkt auf der Open WebUI Website herunter.](https://openwebui.com/f/coleam/n8n_pipe/) (Weitere Anleitungen unten)

![n8n.io - Screenshot](https://raw.githubusercontent.com/n8n-io/self-hosted-ai-starter-kit/main/assets/n8n-demo.gif)

Kuratiert von <https://github.com/n8n-io> und <https://github.com/coleam00>, modifiziert und erweitert von Felix, kombiniert es die self-hosted n8n-Plattform mit einer kuratierten Liste kompatibler AI-Produkte und Komponenten, um schnell mit dem Aufbau von self-hosted AI-Workflows zu beginnen.

### Enthaltene Komponenten

✅ [**Self-hosted n8n**](https://n8n.io/) - Low-Code-Plattform mit über 400
Integrationen und fortschrittlichen AI-Komponenten

✅ [**Ollama**](https://ollama.com/) - Plattformübergreifende LLM-Plattform zur Installation
und Ausführung der neuesten lokalen LLMs

✅ [**Open WebUI**](https://openwebui.com/) - ChatGPT-ähnliches Interface zur
privaten Interaktion mit deinen lokalen Modellen und n8n-Agenten

✅ [**Flowise**](https://flowiseai.com/) - No/Low-Code AI-Agent-Builder,
der sich hervorragend mit n8n kombiniert

✅ [**Qdrant**](https://qdrant.tech/) - Open-Source, hochperformanter Vektorspeicher
mit einer umfassenden API

✅ [**PostgreSQL**](https://www.postgresql.org/) - Arbeitspferd der Data Engineering-Welt, das große Datenmengen sicher verarbeitet

✅ [**Elasticsearch**](https://www.elastic.co/de/elasticsearch) - Dokumenten-/Vektorspeicher

✅ [**Kibana**](https://www.elastic.co/de/kibana) - Dashboard für Elasticsearch

✅ [**Crawl4ai**](https://docs.crawl4ai.com/) - Crawler Container

✅ [**markitdown**](https://github.com/microsoft/markitdown) - File Extractor Container (PDF, OCR, usw.)

## Installation

### Für Nvidia GPU-Nutzer

```
git clone https://github.com/nashtrader/localAIagent.git
cd local-ai-packaged
docker compose --profile gpu-nvidia up
```

> [!HINWEIS]
> Falls du deine Nvidia GPU noch nicht mit Docker verwendet hast, folge bitte den
> [Ollama Docker-Anweisungen](https://github.com/ollama/ollama/blob/main/docs/docker.md).

### Für Mac / Apple Silicon-Nutzer

Falls du einen Mac mit einem M1 oder neueren Prozessor nutzt, kannst du deine GPU
leider nicht für die Docker-Instanz freigeben. Es gibt zwei Möglichkeiten:

1. Das Starter Kit vollständig auf der CPU ausführen (siehe "Für alle anderen" unten)
2. Ollama auf deinem Mac ausführen für schnellere Inferenz und sich mit n8n verbinden

Falls du Ollama auf deinem Mac nutzen möchtest, besuche die
[Ollama Homepage](https://ollama.com/)
für Installationsanweisungen und starte das Starter Kit folgendermaßen:

```
git clone https://github.com/nashtrader/localAIagent.git
cd local-ai-packaged
docker compose up
```

Nach Abschluss der Schnellstart-Einrichtung unten, ändere die Ollama-Anmeldeinformationen,
indem du `http://host.docker.internal:11434/` als Host verwendest.

### Für alle anderen

```
git clone https://github.com/nashtrader/localAIagent.git
cd local-ai-packaged
docker compose --profile cpu up
```

## ⚡️ Schnellstart und Nutzung

Das Hauptbestandteil des Self-hosted AI Starter Kits ist eine vorkonfigurierte Docker-Compose-Datei mit Netzwerk- und Datenträgerunterstützung, sodass nicht viel weiteres installiert werden muss. Nach der Installation folge diesen Schritten:

1. Öffne <http://localhost:5678/> in deinem Browser, um n8n einzurichten. Dies muss nur einmal gemacht werden. Du erstellst hier **kein Konto bei n8n**, sondern nur ein lokales Konto für deine Instanz!
2. Öffne den enthaltenen Workflow: <http://localhost:5678/workflow/vTN9y2dLXqTiDfPT>
3. Erstelle Zugangsdaten für jeden Dienst:

   - **Ollama URL**: `http://ollama:11434`
   - **Postgres**: Nutze die DB, den Benutzernamen und das Passwort aus der `.env`. Host ist `postgres`
   - **Qdrant URL**: `http://qdrant:6333` (API-Schlüssel kann beliebig sein, da es lokal läuft)
   - **Google Drive**: Folge [diesem n8n-Leitfaden](https://docs.n8n.io/integrations/builtin/credentials/google/).
   - **ngrok**: Erstelle dir ein ngrok Account um Webhooks auf deine locale Umgebung zu tunneln.
   - **Telegramm**: Erstelle dir ein Telegramm Account um auch von Unterwegs auf deinen localen Agenten zuzugreifen.

4. Wähle **Test Workflow**, um den Workflow zu starten.
5. Falls es dein erster Start ist, muss Ollama Llama3.1 herunterladen. Überprüfe die Docker-Logs für den Fortschritt.
6. Stelle sicher, dass der Workflow aktiv geschaltet ist und kopiere die "Production" Webhook-URL!
7. Öffne <http://localhost:3000/> im Browser, um Open WebUI einzurichten. Auch hier: **Kein Online-Konto, sondern nur ein lokales Konto!**
8. Gehe zu **Workspace -> Functions -> Add Function**, gib einen Namen und eine Beschreibung ein und füge den Code aus `n8n_pipe.py` ein.
9. Klicke auf das Zahnrad-Symbol und setze `n8n_url` auf die kopierte Webhook-URL.
10. Aktiviere die Funktion, und sie wird nun in deinem Modell-Dropdown verfügbar sein!

## Upgrade-Anweisungen

### Für Nvidia GPU-Nutzer

```
docker compose --profile gpu-nvidia pull
docker compose create && docker compose --profile gpu-nvidia up
```

### Für Mac / Apple Silicon-Nutzer

```
docker compose pull
docker compose create && docker compose up
```

### Für alle anderen

```
docker compose --profile cpu pull
docker compose create && docker compose --profile cpu up
```

## 📜 Lizenz

Dieses Projekt (ursprünglich erstellt vom n8n-Team, Link oben in der README) steht unter der Apache License 2.0 - siehe die
[LICENSE](LICENSE)-Datei für Details.

