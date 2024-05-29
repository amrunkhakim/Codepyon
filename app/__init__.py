from flask import Flask
from config import Config
from .core.database import init_db
from .auth.views import auth_bp
from .main.views import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi database
    init_db(app)

    # Register blueprint untuk modul otentikasi
    app.register_blueprint(auth_bp)

    # Register blueprint untuk modul utama
    app.register_blueprint(main_bp)

    return app
