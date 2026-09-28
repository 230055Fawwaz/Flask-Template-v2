# ==========================================
# Nama File:          __init__.py
# Deskripsi File:     Package initializer untuk modul controller aplikasi
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Mengekspor kelas controller untuk digunakan oleh blueprint routes
#   - Menjaga struktur MVC tetap terorganisir dan bersih
#   - Memastikan pemisahan tugas (Separation of Concerns)
# ==========================================

from app.controllers.item_controller import ItemController

__all__ = ["ItemController"]
