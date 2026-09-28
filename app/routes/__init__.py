# ==========================================
# Nama File:          __init__.py
# Deskripsi File:     Package initializer untuk modul routes blueprint
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Mengekspor blueprint untuk didaftarkan pada Application Factory
#   - Memudahkan pendaftaran modul rute baru di masa mendatang
#   - Menerapkan arsitektur modular yang rapi
# ==========================================

from app.routes.main_routes import main_bp

__all__ = ["main_bp"]
