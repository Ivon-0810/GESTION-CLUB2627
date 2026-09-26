import os
import sys
from flask import Flask

def get_bundle_dir():
    """ Retourne le dossier racine de l'application, compatible PyInstaller (.exe) """
    if getattr(sys, 'frozen', False):
        # L'application tourne sous forme de .exe compilé avec PyInstaller
        return sys._MEIPASS
    # L'application tourne en mode script Python standard
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    base_dir = get_bundle_dir()
    template_folder = os.path.join(base_dir, 'app', 'templates')
    static_folder = os.path.join(base_dir, 'app', 'static')

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    
    # Tes routes et configurations habituelles...
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
