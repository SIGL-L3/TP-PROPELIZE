# TP PROPELIZE - Groupe 08 : Instructions de Configuration et d'Exécution

Ce document détaille les étapes nécessaires pour configurer et lancer l'application PROPELIZE.
**Note Importante sur la Structure des Branches :**
*   Le **Backend** de l'application se trouve sur la branche `main`.
*   Le **Frontend** de l'application (la version à utiliser) se trouve sur la branche `frontend`.

Nous allons donc cloner le dépôt deux fois dans des répertoires distincts, ou utiliser une seule clone et extraire les branches dans des dossiers séparés. Pour plus de clarté, nous allons opter pour une approche de clonage dans des répertoires distincts dédiés au backend et au frontend.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre système :
*   Git
*   Python (version 3.x recommandée) et pip
*   Node.js et npm

## 1. Configuration du Backend (depuis la branche `main`)

### a. Clonage du Dépôt pour le Backend

Ouvrez un terminal et créez un dossier pour le backend, puis clonez-y la branche `main` :
```bash
mkdir propelize_backend
cd propelize_backend
git clone https://github.com/SIGL-L3/TP_PROPELIZE_GROUPE_8.git .
# Par défaut, 'git clone' récupère la branche 'main' (ou la branche par défaut)
```

### b. Création et Activation de l'Environnement Virtuel (pour le Backend)

Toujours dans le dossier `propelize_backend/` :
```bash
# Créer l'environnement virtuel (nommé 'venv' par exemple)
python -m venv venv

# Activer l'environnement virtuel
# Sur Linux/macOS:
source venv/bin/activate
# Sur Windows (cmd.exe):
# venv\Scripts\activate.bat
# Sur Windows (PowerShell):
# venv\Scripts\Activate.ps1
```
Une fois activé, votre invite de commande devrait être préfixée par `(venv)`.

### c. Installation des Dépendances Backend

Toujours dans `propelize_backend/` et avec l'environnement virtuel activé :
```bash
pip install -r requirements.txt
```
*(Assurez-vous que `requirements.txt` se trouve bien à la racine de `propelize_backend/` après le clonage).*

### d. Chargement des Données Initiales (Fixtures)

```bash
python manage.py loaddata initial_data.json
```
*(Assurez-vous que `manage.py` et `initial_data.json` sont accessibles depuis la racine de `propelize_backend/`).*

### e. Lancement du Serveur Backend

Si `manage.py` est à la racine de `propelize_backend/`:
```bash
python manage.py runserver
```
Si, comme dans votre instruction originale, `manage.py` est dans un sous-dossier (par exemple `Backend/` ou `Backend/propelize/`):
```bash
cd Backend/propelize/  # Adaptez ce chemin si nécessaire
python manage.py runserver
# Pour revenir ensuite à la racine de propelize_backend pour les tests: cd ../..
```
Par défaut, le serveur backend sera accessible à l'adresse `http://127.0.0.1:8000/`. **Laissez ce terminal ouvert.**

## 2. Configuration du Frontend (depuis la branche `frontend`)

Ouvrez un **nouveau terminal**.

### a. Clonage du Dépôt pour le Frontend (branche `frontend`)

Créez un dossier distinct pour le frontend et clonez-y spécifiquement la branche `frontend` :
```bash
mkdir propelize_frontend_code
cd propelize_frontend_code
git clone --branch frontend https://github.com/SIGL-L3/TP_PROPELIZE_GROUPE_8.git .
```

### b. Navigation vers le Dossier Applicatif Frontend

D'après votre instruction originale, le code source du frontend se trouve dans un sous-dossier. Naviguez-y :
```bash
# Depuis propelize_frontend_code/
cd Frontend/PropelizeFrontend  # Adaptez si le chemin est différent dans la branche 'frontend'
```

### c. Installation des Dépendances Frontend

Dans `propelize_frontend_code/Frontend/PropelizeFrontend/` :
```bash
npm install
```

### d. Lancement du Serveur de Développement Frontend

```bash
npm run dev
```
Le serveur frontend sera généralement accessible à une adresse comme `http://localhost:3000/` ou `http://localhost:5173/` (vérifiez la sortie du terminal pour l'URL exacte). **Laissez ce terminal ouvert.**

## 3. Exécution des Tests Unitaires (Backend)

Ouvrez un **troisième terminal** (ou réutilisez celui du backend après avoir arrêté le serveur).

Naviguez vers le dossier du backend et activez l'environnement virtuel s'il ne l'est pas :
```bash
cd chemin/vers/votre/propelize_backend
source venv/bin/activate  # ou équivalent Windows
```

### a. Tests Spécifiques aux Applications

Si `manage.py` est à la racine de `propelize_backend/`:
```bash
python manage.py test vehicule
python manage.py test user
```
Si `manage.py` est dans un sous-dossier (ex: `Backend/propelize/`), placez-vous dans ce sous-dossier pour exécuter les tests ou ajustez le chemin vers `manage.py`. Cependant, les tests sont généralement lancés depuis le répertoire contenant `manage.py`.

### b. Rapport de Couverture des Tests

```bash
coverage run manage.py test
coverage report
```
Pour un rapport HTML plus détaillé (recommandé) :
```bash
coverage html
```
Ouvrez ensuite le fichier `htmlcov/index.html` (qui sera dans `propelize_backend/htmlcov/`) dans votre navigateur.

## Résumé des Opérations

**Pour le Backend (Terminal 1) :**
1.  `mkdir propelize_backend && cd propelize_backend`
2.  `git clone https://github.com/SIGL-L3/TP_PROPELIZE_GROUPE_8.git .`
3.  `python -m venv venv && source venv/bin/activate`
4.  `pip install -r requirements.txt`
5.  `python manage.py loaddata initial_data.json`
6.  `cd Backend/propelize/` (ou l'emplacement de votre `manage.py` si différent pour `runserver`)
7.  `python manage.py runserver`

**Pour le Frontend (Terminal 2) :**
1.  `mkdir propelize_frontend_code && cd propelize_frontend_code`
2.  `git clone --branch frontend https://github.com/SIGL-L3/TP_PROPELIZE_GROUPE_8.git .`
3.  `cd Frontend/PropelizeFrontend`
4.  `npm install`
5.  `npm run dev`

**Pour les Tests (Terminal 3, depuis `propelize_backend/` avec venv activé) :**
1.  `python manage.py test vehicule`
2.  `python manage.py test user`
3.  `coverage run manage.py test && coverage report`
