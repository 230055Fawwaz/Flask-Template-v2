# ==========================================
# Nama File:          test_services.py
# Deskripsi File:     Pengujian unit untuk modul ItemService
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  28-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Menguji logika bisnis CRUD dan query database
#   - Memastikan penanganan input valid dan tidak valid
# ==========================================

from app.services.item_service import ItemService


def test_create_item_success(app):
    """Menguji penambahan item baru dengan data yang valid."""
    success, item = ItemService.create_item(
        title="Belajar Pytest",
        description="Menulis pengujian otomatis untuk Flask",
    )
    assert success is True
    assert item.id is not None
    assert item.title == "Belajar Pytest"
    assert item.description == "Menulis pengujian otomatis untuk Flask"
    assert item.is_completed is False


def test_create_item_empty_title(app):
    """Menguji pembuatan item dengan judul kosong ditolak."""
    success, message = ItemService.create_item(title="   ", description="Tidak ada judul")
    assert success is False
    assert "tidak boleh kosong" in message


def test_get_all_items(app):
    """Menguji pengambilan seluruh daftar item."""
    ItemService.create_item(title="Item Pertama")
    ItemService.create_item(title="Item Kedua")

    items = ItemService.get_all_items()
    assert len(items) == 2
    assert items[0].title == "Item Kedua"  # Urutan desc (terbaru lebih dahulu)


def test_get_item_by_id(app):
    """Menguji pencarian item berdasarkan ID spesifik."""
    _, created = ItemService.create_item(title="Item Spesifik")
    found = ItemService.get_item_by_id(created.id)

    assert found is not None
    assert found.title == "Item Spesifik"

    not_found = ItemService.get_item_by_id(9999)
    assert not_found is None


def test_toggle_item_status(app):
    """Menguji pengubahan status penyelesaian item."""
    _, item = ItemService.create_item(title="Tugas Belum Selesai")
    assert item.is_completed is False

    success, updated = ItemService.toggle_item_status(item.id)
    assert success is True
    assert updated.is_completed is True

    # Toggle kembali
    success, updated_again = ItemService.toggle_item_status(item.id)
    assert success is True
    assert updated_again.is_completed is False


def test_toggle_item_not_found(app):
    """Menguji toggle item yang tidak ada di database."""
    success, message = ItemService.toggle_item_status(9999)
    assert success is False
    assert "tidak ditemukan" in message


def test_delete_item(app):
    """Menguji penghapusan item dari database."""
    _, item = ItemService.create_item(title="Item Dihapus")
    success, message = ItemService.delete_item(item.id)

    assert success is True
    assert "berhasil dihapus" in message
    assert ItemService.get_item_by_id(item.id) is None


def test_delete_item_not_found(app):
    """Menguji penghapusan item dengan ID yang tidak valid."""
    success, message = ItemService.delete_item(9999)
    assert success is False
    assert "tidak ditemukan" in message
