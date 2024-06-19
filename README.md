# multilang_site

## Description

Ce projet est une application Django simple et multilingue permettant de gérer et d'afficher des articles de blog. L'application inclut également une fonctionnalité optionnelle de chatbot utilisant un modèle de langage (GPT-3) et une recherche augmentée par intelligence artificielle (RAG).

## Fonctionnalités

- Gestion des articles de blog avec titre, contenu et date de publication
- Support de l'internationalisation (i18n) avec deux langues : français et anglais
- Interface utilisateur permettant de changer la langue de l'interface
- (Optionnel) Intégration d'un chatbot utilisant GPT-3
- (Optionnel) Fonctionnalité de recherche augmentée par intelligence artificielle (RAG)

## Prérequis

- Python 3.7+
- Django 3.0+
- Un compte OpenAI pour utiliser l'API GPT-3 (si vous intégrez le chatbot)

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/Olivier-Kazadi/multilang_site.git
    cd multilang_site
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :

    ```bash
    python manage.py migrate
    ```

5. Créez un superutilisateur pour accéder à l'interface d'administration Django :

    ```bash
    python manage.py createsuperuser
    ```

6. Compilez les fichiers de traduction :

    ```bash
    django-admin compilemessages
    ```

7. Exécutez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

## Utilisation

- Accédez à l'interface d'administration à `http://127.0.0.1:8000/admin/` pour ajouter des articles de blog.
- Accédez à la page principale à `http://127.0.0.1:8000/` pour voir la liste des articles de blog.
- Utilisez le sélecteur de langue en bas de page pour changer la langue de l'interface.
- (Optionnel) Accédez à la page du chatbot à `http://127.0.0.1:8000/chatbot/` pour interagir avec le modèle GPT-3.

## Configuration pour le Chatbot (Optionnel)

1. Ajoutez votre clé API OpenAI dans le fichier `settings.py` :

    ```python
    OPENAI_API_KEY = 'votre-clé-api-openai'
    ```

2. Assurez-vous que la vue et le template du chatbot sont configurés correctement.

## Déploiement

Vous pouvez déployer ce projet sur Render.com ou toute autre plateforme de déploiement gratuite. Assurez-vous de configurer les variables d'environnement nécessaires, notamment `OPENAI_API_KEY` si vous utilisez le chatbot.

## Auteurs

Ce projet a été réalisé dans le cadre d'un test technique pour une alternance chez Diot-Siaci.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
