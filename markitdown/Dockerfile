FROM python:3.13-slim-bullseye

USER root

ARG INSTALL_GIT=false
RUN if [ "$INSTALL_GIT" = "true" ]; then \
    apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*; \
    fi

# Runtime dependency
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Installiere MarkItDown & Flask
RUN pip install markitdown flask

# Kopiere das Webserver-Skript in das Docker-Image
COPY markitdown_server.py /app/markitdown_server.py

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Standard-Nutzer setzen
ARG USERID=10000
ARG GROUPID=10000
USER $USERID:$GROUPID

# Starte den Flask-Server
CMD ["python", "markitdown_server.py"]
