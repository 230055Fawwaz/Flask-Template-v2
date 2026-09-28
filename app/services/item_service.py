# ==========================================
# Nama File:          item_service.py
# Deskripsi File:     Service untuk menangani logika bisnis entitas Item
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  28-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Memisahkan logika manipulasi database dari layer presentasi (routes)
#   - Menggunakan pendekatan SQLAlchemy modern (db.session.get & db.select)
#   - Menyediakan return value berupa tuple (status_sukses, data_atau_pesan)
# ==========================================

from app.extensions import db
from app.models.item_model import Item


class ItemService:
    """Service layer untuk mengelola operasi bisnis dan query data Item."""

    @staticmethod
    def get_all_items() -> list[Item]:
        """Mengambil seluruh data item diurutkan dari yang paling baru."""
        query = db.select(Item).order_by(Item.created_at.desc())
        return list(db.session.scalars(query).all())

    @staticmethod
    def get_item_by_id(item_id: int) -> Item | None:
        """Mengambil satu data item berdasarkan ID entitas."""
        return db.session.get(Item, item_id)

    @staticmethod
    def create_item(title: str, description: str | None = None) -> tuple[bool, Item | str]:
        """Membuat item baru dan menyimpannya ke database."""
        clean_title = (title or "").strip()
        if not clean_title:
            return False, "Judul item tidak boleh kosong."

        try:
            new_item = Item(
                title=clean_title,
                description=(description or "").strip() or None,
            )
            db.session.add(new_item)
            db.session.commit()
            return True, new_item
        except Exception as error:
            db.session.rollback()
            return False, f"Gagal membuat item: {error}"

    @staticmethod
    def toggle_item_status(item_id: int) -> tuple[bool, Item | str]:
        """Mengubah status penyelesaian (is_completed) dari suatu item."""
        item = db.session.get(Item, item_id)
        if not item:
            return False, "Item tidak ditemukan."

        try:
            item.is_completed = not item.is_completed
            db.session.commit()
            return True, item
        except Exception as error:
            db.session.rollback()
            return False, f"Gagal memperbarui status item: {error}"

    @staticmethod
    def delete_item(item_id: int) -> tuple[bool, str]:
        """Menghapus item dari database berdasarkan ID."""
        item = db.session.get(Item, item_id)
        if not item:
            return False, "Item tidak ditemukan."

        try:
            db.session.delete(item)
            db.session.commit()
            return True, "Item berhasil dihapus."
        except Exception as error:
            db.session.rollback()
            return False, f"Gagal menghapus item: {error}"
