
from extensions import db
from sqlalchemy import text
from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt




biblioteque_bp = Blueprint('biblioteque', __name__)
bcrypt = Bcrypt()



@biblioteque_bp.route('/bibliotheques', methods=['GET'])
def get_bibliotheques():
    result = db.session.execute(text("SELECT * FROM bibliotheque")).fetchall()
    data = [dict(row._mapping) for row in result]
    return jsonify({"bibliotheques": data})

@biblioteque_bp.route('/livres', methods=['GET'])
def get_livres():
    result = db.session.execute(text("SELECT * FROM livre")).fetchall()
    data = [dict(row._mapping) for row in result]
    return jsonify({"livres": data})


@biblioteque_bp.route('/ajouter_livre', methods=['POST'])
def post_livre():
    data = request.json
    titre = data['titre']
    auteur = data['auteur']
    

    # Ajouter le livre à la base de données
    # ici les categories et bibliotheques sont hardcodés pour l'instant, à changer plus tard
    db.session.execute(text(
        "INSERT INTO livre (titre, auteur, statut, id_categorie, id_bibliotheque) VALUES (:titre, :auteur, 'disponible', 1, 1)"
    ), {"titre": titre, "auteur": auteur})
    db.session.commit()
    
    return jsonify({"message": "Livre ajouté !"})