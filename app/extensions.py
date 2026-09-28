# ==========================================
# Nama File:          extensions.py
# Deskripsi File:     Inisialisasi ekstensi pihak ketiga Flask
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Mencegah circular import dengan inisialisasi ekstensi tanpa app
#   - Menyediakan instance SQLAlchemy untuk model database
#   - Menyediakan instance Flask-Migrate untuk pelacakan skema DB
# ==========================================

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instance database ORM
db = SQLAlchemy()

# Instance database migration engine
migrate = Migrate()
