# Étape 1 : Image de base avec Python + Node + Playwright
FROM mcr.microsoft.com/playwright:v1.41.1-focal

# Définir le dossier principal
WORKDIR /app

# 🔹 Copier et installer le backend Django
COPY propelize/ ./propelize/
COPY propelize/manage.py ./propelize/manage.py
COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 🔹 Copier et installer le frontend Vue + Playwright
COPY propelizeFrontend/ ./propelizeFrontend/

WORKDIR /app/propelizeFrontend
RUN npm install && npx playwright install --with-deps

#  Exposer les ports nécessaires
 # Django
 EXPOSE 8000  
  # Vue.js (si tu lances aussi l'UI depuis ce conteneur) 
 EXPOSE 3000   
#  Lancer uniquement Django (version standard)
WORKDIR /app/propelize
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#  Facultatif : tu peux créer un second Dockerfile juste pour le front
