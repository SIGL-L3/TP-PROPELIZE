# 🚀 TP_PROPELIZE_GROUPE_8

**Propelize** est une application web complète qui gère des entités(Vehicule) via une interface frontend moderne et un backend Django robuste. Ce projet a été réalisé dans le cadre d’un TP académique de fin d’unité.

---------------------

## 📁 Structure du projet


TP_PROPELIZE_GROUPE_8/
├── PropelizeFrontend/       # Frontend Vue.js (Vite)
├── propelize/               # Backend Django + API REST
├── db.sqlite3               # Base de données SQLite
├── ci-cd.png                # Diagramme du pipeline CI/CD
└── README.md


---------------------
## Cloner le Projet
Pour avoir le projet , il faut le cloner via git clone https://github.com/SIGL-L3/TP_PROPELIZE_GROUPE_8
ensuite cloner la branche Frontend dans un autre repertoire puis Lancer les deux serveux 
## 🛠️ Stack technique

### Frontend
- [Vue.js](https://vuejs.org/) 3
- [Vite](https://vitejs.dev/)
- [Cypress](https://www.cypress.io/) (tests end-to-end)

### Backend
- [Python 3](https://www.python.org/)
- [Django 4+](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- SQLite (base de données légère embarquée)

---------------------

## ⚙️ Installation

### Pré-requis

- Node.js ≥ 18.x
- Python ≥ 3.10
- pip, venv
- Git

### Backend


cd propelize
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


### Frontend


cd PropelizeFrontend
npm install
npm run dev


--------------------

## 🧪 Tests

### Backend (Django)


cd propelize
python manage.py test user.tests vehicules.tests 
# Un rapport de couverture peut être généré via coverage.py si installé :
coverage run manage.py test user.tests vehicule.tests
coverage report
coverage html
# Le rapport sera généré dans htmlcov/

### Frontend (Cypress)


cd PropelizeFrontend
npx cypress open
# OU
npx cypress run
## Note: les  serveurs doivent etres lancer au prealable


----------------------

## 🔌 API REST (Exemples)

- 'GET /api/vehicules/' – Liste des véhicules
- 'POST /api/vehicules/' – Création
- 'PUT /api/vehicules/<id>/' – Mise à jour
- DELETE /api/vehicules/<id>/' – Suppression

> L'API suit la structure REST classique définie dans Django REST Framework.

----------------------

## 📸 Présentation CI/CD

Une image ci-cd.png est incluse pour illustrer notre pipeline d’intégration continue.

-------------------------

## 🤝 Contribuer

1. Fork le repo
2. Crée une branche 'feature/ma-nouvelle-feature'
3. Commit tes modifications
4. Ouvre une Pull Request

------------------------

## 📄 Licence

Ce projet est sous licence **MIT**. Voir 'LICENSE' pour plus d'informations.

------------------------

## 👥 Auteurs

Projet réalisé par le **Groupe 8** dans le cadre du TP PROPELIZE.  
Encadré par Dr KIMBI Xaveria et Mr Regis ATEMENGUE Enseignant de  SIGL L3 a l'universite de yaounde 1 .
