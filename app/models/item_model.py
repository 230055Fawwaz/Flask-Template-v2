# ==========================================
# Nama File:          item_model.py
# Deskripsi File:     Model entitas Item untuk demonstrasi database ORM
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Representasi tabel 'items' di SQLite menggunakan Flask-SQLAlchemy
#   - Menyimpan data judul, deskripsi, status selesai, dan timestamp
#   - Mengimplementasikan metode to_dict untuk kemudahan serialisasi
# ==========================================

from datetime import datetime, timezone
from app.extensions import db


class Item(db.Model):
    """Model entitas Item untuk demonstrasi CRUD."""
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    def to_dict(self):
        """Konversi objek model ke kamus (dictionary)."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
            "created_at": self.created_at.strftime("%d-%m-%Y %H:%M:%S") if self.created_at else None
        }

    def __repr__(self):
        return f"<Item id={self.id} title='{self.title}'>"
