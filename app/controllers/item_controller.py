# ==========================================
# Nama File:          item_controller.py
# Deskripsi File:     Controller untuk menangani logika bisnis entitas Item
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Bertanggung jawab memproses manipulasi data CRUD entitas Item
#   - Memisahkan logika query dan transaksi database dari layer routing
#   - Menyediakan return value yang konsisten untuk digunakan oleh route
# ==========================================

from app.extensions import db
from app.models.item_model import Item


class ItemController:
    """Controller pengelola operasi logika data Item."""

    @staticmethod
    def get_all_items():
        """Mengambil seluruh data item diurutkan dari yang terbaru."""
        return Item.query.order_by(Item.created_at.desc()).all()

    @staticmethod
    def get_item_by_id(item_id):
        """Mengambil satu data item berdasarkan ID."""
        return Item.query.get(item_id)

    @staticmethod
    def create_item(title, description=None):
        """Membuat item baru dan menyimpannya ke database."""
        clean_title = (title or "").strip()
        if not clean_title:
            return False, "Judul item tidak boleh kosong."

        try:
            new_item = Item(
                title=clean_title,
                description=(description or "").strip() or None
            )
            db.session.add(new_item)
            db.session.commit()
            return True, new_item
        except Exception as error:
            db.session.rollback()
            return False, f"Gagal membuat item: {str(error)}"

    @staticmethod
    def toggle_item_status(item_id):
        """Mengubah status penyelesaian (is_completed) dari item."""
        item = Item.query.get(item_id)
        if not item:
            return False, "Item tidak ditemukan."

        try:
            item.is_completed = not item.is_completed
            db.session.commit()
            return True, item
        except Exception as error:
            db.session.rollback()
            return False, f"Gagal memperbarui status item: {str(error)}"

    @staticmethod
    def delete_item(item_id):
        """Menghapus item dari database."""
        item = Item.query.get(item_id)
        if not item:
            return False, "Item tidak ditemukan."

        try:
            db.session.delete(item)
            db.session.commit()
            return True, "Item berhasil dihapus."
        except Exception as error:
            db.session.rollback()
            return False, f"Gagal menghapus item: {str(error)}"
