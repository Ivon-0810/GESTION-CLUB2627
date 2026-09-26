from app.routes.main import main_bp
from app.routes.effectif import effectif_bp
from app.routes.match_routes import match_bp
from app.routes.mercato import mercato_bp
from app.routes.palmares import palmares_bp
from app.routes.recherche import recherche_bp
from app.routes.saison import saison_bp

__all__ = [
    'main_bp',
    'effectif_bp',
    'match_bp',
    'mercato_bp',
    'palmares_bp',
    'recherche_bp',
    'saison_bp'
]
