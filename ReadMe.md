# Setup du Serveur Backend

Ce projet utilise Flask pour le backend avec SQLAlchemy pour gérer la base de données MySQL.

## Prérequis

- Python 3.8+
- MySQL Server (pour la base de données)
- pip (gestionnaire de paquets Python)

---

## Étape 1 : Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
```

Activez l'environnement :

- **Windows** : `venv\Scripts\activate`
- **Mac/Linux** : `source venv/bin/activate`

---

## Étape 2 : Installer les dépendances

Installez tous les modules requis :

```bash
pip install -r requirements.txt
```

### Modules nécessaires :

- **Flask** - Framework web Python
- **Flask-CORS** - Gestion des CORS (Cross-Origin Resource Sharing)
- **Flask-SQLAlchemy** - ORM pour gérer la base de données
- **PyMySQL** - Driver pour la connexion MySQL
- **Flask-Bcrypt** - Hachage sécurisé des mots de passe

Si `requirements.txt` n'existe pas, installez manuellement :

```bash
pip install Flask Flask-CORS Flask-SQLAlchemy PyMySQL Flask-Bcrypt
```

---

## Étape 3 : Configurer la base de données

### Configuration MySQL

Assurez-vous que MySQL est installé et en cours d'exécution.

La chaîne de connexion est définie dans `app.py` :

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jesuisbeau@localhost/bibliotheque'
```

**À modifier si nécessaire :**

- `root` → votre username MySQL
- `jesuisbeau` → votre mot de passe MySQL
- `localhost` → votre host MySQL
- `bibliotheque` → nom de votre base de données

### Créer la base de données

Ouvrez MySQL et exécutez ces commandes :

```sql
CREATE DATABASE bibliotheque;
USE bibliotheque;

-- Table adhérents
CREATE TABLE adherent (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(50) NOT NULL,
  prenom VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  adherent_passw VARCHAR(255) NOT NULL
);

-- Table livres
CREATE TABLE livre (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titre VARCHAR(150) NOT NULL,
  auteur VARCHAR(100) NOT NULL,
  isbn VARCHAR(50),
  status VARCHAR(30) NOT NULL
);

-- Table bibliothèques
CREATE TABLE bibliotheque (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(100) NOT NULL,
  adresse VARCHAR(150)
);
```

---

## Étape 4 : Lancer le serveur

Une fois les dépendances installées et la base de données configurée :

```bash
python app.py
```

Le serveur démarrera sur `http://127.0.0.1:5000`

Vous devriez voir :

```
 * Running on http://127.0.0.1:5000
```

---

## Étape 5 : Vérifier la connexion

Ouvrez votre navigateur et allez à :

```
http://localhost:5000/
```

Vous devriez voir la réponse JSON :

```json
{ "message": "Server running!" }
```

---

## Endpoints disponibles

### Authentication

- **POST** `/register` - Créer un nouvel administrateur
- **POST** `/login` - Se connecter

### Gestion des livres

- **GET** `/livres` - Récupérer tous les livres
- **GET** `/bibliotheques` - Récupérer toutes les bibliothèques
- **POST** `/ajouter_livre` - Ajouter un nouveau livre

---

## Architecture du serveur

```
python_server/
├── app.py                 # Point d'entrée principal
├── extensions.py          # Configuration SQLAlchemy
├── authAdmin.py          # Routes d'authentification
├── biblioteque.py        # Routes de gestion des livres
├── requirements.txt      # Dépendances Python
└── ReadMe.md            # Ce fichier
```

---

## Troubleshooting

### Erreur : "No module named 'flask'"

Assurez-vous d'avoir exécuté `pip install -r requirements.txt`

### Erreur : "Cannot connect to MySQL"

- Vérifiez que MySQL est en cours d'exécution
- Vérifiez les credentials dans `app.py`
- Vérifiez que la base de données `bibliotheque` existe

### CORS errors

Les CORS sont configurés avec `CORS(app)` dans `app.py`. Si vous avez des problèmes, vérifiez que le frontend utilise la bonne URL.

---

## Notes de développement

- Le serveur tourne en mode `debug=True` par défaut. À désactiver en production !
- Les mots de passe sont hachés avec Bcrypt pour la sécurité
- Les requêtes utilisent des paramètres nommés pour prévenir les injections SQL
- CORS est activé pour permettre les requêtes crossorigin depuis le frontend
