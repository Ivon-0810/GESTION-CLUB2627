import os
import sys
from flask import Flask
from app.extensions import db

def get_bundle_dir():
    """ Retourne le dossier racine de l'application, compatible PyInstaller (.exe) """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    base_dir = get_bundle_dir()
    template_folder = os.path.join(base_dir, 'app', 'templates')
    static_folder = os.path.join(base_dir, 'app', 'static')

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

    # Configuration de la base de données SQLite
    db_path = os.path.join(os.path.dirname(base_dir), 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'cle_secrete_gestion_club'

    # Liaison indispensable de SQLAlchemy à l'application Flask
    db.init_app(app)

    # Importation et enregistrement des routes/blueprints
    from app.routes import (
        main_bp,
        effectif_bp,
        match_bp,
        mercato_bp,
        palmares_bp,
        recherche_bp,
        saison_bp
    )

    app.register_blueprint(main_bp)
    app.register_blueprint(effectif_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(mercato_bp)
    app.register_blueprint(palmares_bp)
    app.register_blueprint(recherche_bp)
    app.register_blueprint(saison_bp)

    return app
