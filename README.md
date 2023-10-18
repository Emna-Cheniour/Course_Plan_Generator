# Création d'une API de suggestion de Plan de cours à partir d’un contenu PDF
## Description
Ce projet est un générateur de plans de cours éducatifs basés sur le contenu extrait de documents PDF en ligne. Il utilise le framework FastAPI qui prend en entrée un lien vers un document PDF en ligne, fait extraire son contenu, génère un plan de cours en utilisant OpenAI GPT-3.5, et finalement le rend en format markdown.
- Le générateur de plan de cours de cette API utilise un prompt spécialisé qui inclut l'approche 'certif' pour assurer la création de plans de cours pertinents et structurés.

## Prérequis
- Python 3.11.3
- FastAPI
- OpenAI
- PyPDF2
- Markdown2
- Langchain

## Installation
1. Faire cloner ce répertoire sur votre machine.
2. Installez les dépendances en utilisant `pip install -r requirements.txt`.
3. Configurez la variable d'environnement `OPENAI_API_KEY`, avec votre clé API OpenAI.

## Utilisation
Vous pouvez utiliser cette API pour générer des plans de cours basés sur des fichiers PDF en ligne. Voici comment utiliser l'API :

1. Exécutez le serveur avec `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`.
2. Faites une requête GET à `http://localhost:8000/course_plan` avec les paramètres suivants :
   - `pdf_url` : L'URL du PDF en ligne.
   - `token` : Votre clé API OpenAI.

## Structure du Projet
- `main.py` : Le fichier principal qui définit l'API FastAPI.
- `prompts.py` : Le fichier qui stocke les prompts spécifiques utilisés pour interagir avec l'API OpenAI.
- `utils.py` : Le fichier qui contient diverses fonctions utilitaires pour notre API.
- `requirements.txt` : Liste des dépendances du projet.
- `README.md` : La documentation que vous lisez actuellement.
- `tests\test_main.py` : Le fichier des tests unitaires qui vérifient le bon fonctionnement de l'API FastAPI. Les tests couvrent différents cas, notamment la génération de plans de cours réussie, la gestion des erreurs liées aux clés API OpenAI, la manipulation des URL PDF invalides et la validation de la qualité du format Markdown généré.

