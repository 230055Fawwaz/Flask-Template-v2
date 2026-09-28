# ==========================================
# Nama File:          __init__.py
# Deskripsi File:     Application Factory untuk inisialisasi aplikasi Flask
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Menerapkan pola Application Factory (create_app)
#   - Menginisialisasi ekstensi SQLAlchemy dan Migrate
#   - Mendaftarkan blueprint routes ke instance aplikasi
# ==========================================

from flask import Flask
from app.config import DevelopmentConfig
from app.extensions import db, migrate
from app.routes.main_routes import main_bp
import app.models  # Pastikan seluruh model terdaftar untuk Alembic/Flask-Migrate


def create_app(config_class=DevelopmentConfig):
    """Fungsi pabrik (Application Factory) untuk membuat instance Flask."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inisialisasi ekstensi database dan migrasi
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrasi Blueprints
    app.register_blueprint(main_bp)

    # Inisialisasi tabel database saat pertama kali dijalankan (kemudahan mode dev)
    with app.app_context():
        db.create_all()

    return app
