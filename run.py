import sys
import threading
import webbrowser

from app import create_app
from app.extensions import db
from app.data.seed_data import peupler_base
from app.data.generateur_joueurs import generer_effectifs
from app.data.generateur_entraineurs import generer_entraineurs
from app.services.calendrier_saison import generer_calendrier_saison_complete
from app.models import Saison

app = create_app()

def _ouvrir_navigateur():
    """ Ouvre automatiquement le navigateur web sur l'application """
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    # 1. Initialisation de la base de données au lancement principal
    with app.app_context():
        db.create_all()
        peupler_base()
        generer_effectifs()
        generer_entraineurs()
        
        saison_courante = Saison.query.filter_by(est_courante=True).first()
        if saison_courante:
            generer_calendrier_saison_complete(saison_courante)

    # 2. Gestion du mode .exe (PyInstaller)
    est_fige = getattr(sys, "frozen", False)
    
    # 3. Ouverture automatique du navigateur
    threading.Timer(1.2, _ouvrir_navigateur).start()
    
    # 4. Lancement du serveur Flask
    app.run(debug=not est_fige, port=5000, use_reloader=False)
