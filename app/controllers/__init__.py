# ==========================================
# Nama File:          __init__.py
# Deskripsi File:     Package initializer controllers (Deprecated - Dialihkan ke services)
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Deprecated di v2: Gunakan package 'app.services'
#   - Disediakan untuk kompatibilitas mundur (backward compatibility)
# ==========================================

from app.services.item_service import ItemService as ItemController

__all__ = ["ItemController"]
