# ==========================================
# Nama File:          config.py
# Deskripsi File:     Pengaturan konfigurasi lingkungan aplikasi Flask
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  29-09-2026
# Catatan:
#   - Memisahkan konfigurasi Development, Testing, dan Production
#   - Menggunakan SQLite sebagai default database engine
#   - Memanfaatkan python-dotenv untuk membaca variabel .env
#   - Mengontrol inisialisasi tabel otomatis (AUTO_CREATE_TABLES) untuk offline-first
# ==========================================

import os
from pathlib import Path
from dotenv import load_dotenv

# Path direktori dasar proyek (root)
BASE_DIR = Path(__file__).resolve().parent.parent

# Muat file .env jika tersedia
load_dotenv(BASE_DIR / ".env")


class Config:
    """Konfigurasi dasar (Base Configuration)."""
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTO_CREATE_TABLES = False

    # Direktori instance untuk database SQLite
    INSTANCE_PATH = BASE_DIR / "instance"
    INSTANCE_PATH.mkdir(exist_ok=True)

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{INSTANCE_PATH / 'app.db'}"
    )


class DevelopmentConfig(Config):
    """Konfigurasi untuk lingkungan pengembangan (Development)."""
    DEBUG = True
    AUTO_CREATE_TABLES = True  # Otomatis buat tabel SQLite saat pertama kali clone proyek


class TestingConfig(Config):
    """Konfigurasi untuk lingkungan pengujian otomatis (Testing)."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    AUTO_CREATE_TABLES = True  # Database in-memory memerlukan tabel baru di setiap sesi test


class ProductionConfig(Config):
    """Konfigurasi untuk lingkungan rilis/produksi (Production)."""
    DEBUG = False
    TESTING = False
    # Pada aplikasi offline-first / standalone, tabel SQLite otomatis dibuat saat start-up
    # agar pengguna tidak perlu menjalankan CLI migrasi manual saat rilis pertama kali.
    AUTO_CREATE_TABLES = os.getenv("AUTO_CREATE_TABLES", "True").lower() in ("true", "1", "yes")


# Pemetaan konfigurasi berdasarkan nama lingkungan
config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
