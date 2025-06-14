# ====== Étape 1 : Backend + Frontend + Cypress build ======
FROM python:3.11-slim AS builder

# Dépendances système
RUN apt-get update && apt-get install -y \
    curl gnupg git build-essential libpq-dev && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Répertoire de travail
WORKDIR /app

# Backend
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le backend
COPY propelize/ ./propelize/
COPY propelize/manage.py ./propelize/manage.py

# Frontend + Cypress
COPY propelizeFrontend/ ./propelizeFrontend/
WORKDIR /app/propelizeFrontend
RUN npm install && npm install --save-dev cypress

# ====== Étape 2 : Exécution de tests avec Cypress (séparé) ======
FROM cypress/included:12.17.1 AS cypress-runner
COPY --from=builder /app/propelizeFrontend /app/propelizeFrontend
WORKDIR /app/propelizeFrontend
CMD ["npx", "cypress", "run"]

# ====== Étape 3 : Image finale pour exécution du backend ======
FROM python:3.11-slim

WORKDIR /app

# Dépendances système
RUN apt-get update && apt-get install -y libpq-dev curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copier depuis builder
COPY --from=builder /app /app

# Exposer les ports
EXPOSE 8000
EXPOSE 3000

# Entrée pour lancer Django
CMD ["python", "propelize/manage.py", "runserver", "0.0.0.0:8000"]
