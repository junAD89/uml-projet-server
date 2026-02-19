from flask import Flask, jsonify
from flask_cors import CORS
from authAdmin import auth_bp
from biblioteque import biblioteque_bp
from extensions import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jesuisbeau@localhost/bibliotheque'

db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(biblioteque_bp)

@app.route('/')
def index():
    return jsonify({"message": "Server running!"})

if __name__ == '__main__':
    app.run(debug=True)