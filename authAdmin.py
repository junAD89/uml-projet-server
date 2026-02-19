
from extensions import db
from sqlalchemy import text
from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt




auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()



@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    nom = data['adminNom']
    prenom = data['adminPrenom']
    email = data['adminEmail']
    password = data['adminPassword']
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    print(f"email: {email}")
    print(f"nom: {nom}")
    db.session.execute(text(
        "INSERT INTO adherent (nom, prenom, email, adherent_passw) VALUES (:nom, :prenom, :email, :passw)"
    ), {"nom": nom, "prenom": prenom, "email": email, "passw": hashed})
    db.session.commit()
    return jsonify({"message": "Données reçues !", "nom": nom, "email": email})
 



@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json 
    email = data['adminEmail']
    password = data['adminPassword']
    result = db.session.execute(text(
        "SELECT * FROM adherent WHERE email = :email"
    ), {"email": email}).first()
      
    if result and bcrypt.check_password_hash(result.adherent_passw, password):
        return jsonify({"message": "Connecté !", "nom": result.nom})
    else:
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401
    return jsonify({"message": "Login reçu"})

