# ==========================================
# Nama File:          __init__.py
# Deskripsi File:     Package initializer untuk modul model database
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Mengekspor model agar dapat diimpor langsung dari app.models
#   - Memudahkan pendaftaran model ke sistem migrasi Flask-Migrate
#   - Menerapkan prinsip modularitas dan kerapihan arsitektur
# ==========================================

from app.models.item_model import Item

__all__ = ["Item"]
