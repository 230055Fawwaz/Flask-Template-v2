# ==========================================
# Nama File:          item_controller.py
# Deskripsi File:     ItemController (Deprecated - Dialihkan ke ItemService)
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Deprecated di v2: Gunakan 'app.services.item_service.ItemService'
#   - Mempertahankan kompatibilitas bagi kode yang masih mengimpor ItemController
# ==========================================

from app.services.item_service import ItemService as ItemController

__all__ = ["ItemController"]
