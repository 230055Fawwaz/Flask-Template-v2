# ==========================================
# Nama File:          test_routes.py
# Deskripsi File:     Pengujian integrasi untuk endpoint routes dan respons HTMX
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  28-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Menguji halaman beranda, endpoint form standar, dan respons partial HTMX
#   - Menguji endpoint REST API JSON
# ==========================================

from app.services.item_service import ItemService


def test_index_route(client):
    """Menguji render halaman beranda mengembalikan status HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Flask Modern Template" in response.get_data(as_text=True)


def test_create_item_standard_route(client):
    """Menguji penambahan item melalui submit formulir standar (redirect)."""
    response = client.post(
        "/items/create",
        data={"title": "Item Standar", "description": "Tanpa HTMX"},
        follow_redirects=False,
    )
    # Redirect 302 kembali ke beranda
    assert response.status_code == 302
    assert response.headers["Location"] == "/"


def test_create_item_htmx_route(client):
    """Menguji penambahan item via permintaan AJAX HTMX (mengembalikan partial HTML)."""
    response = client.post(
        "/items/create",
        data={"title": "Item HTMX", "description": "Dengan HTMX header"},
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    # Mengembalikan partial _item_list.html tanpa tag <html> penuh
    assert "items-list-container" in html
    assert "Item HTMX" in html


def test_toggle_item_htmx_route(client, app):
    """Menguji toggle status item via HTMX (mengembalikan partial _item_row.html)."""
    _, item = ItemService.create_item(title="Item Uji Toggle")

    response = client.post(
        f"/items/toggle/{item.id}",
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert f"item-entry-{item.id}" in html
    assert "Selesai" in html


def test_delete_item_htmx_route(client, app):
    """Menguji penghapusan item via HTMX (mengembalikan partial _item_list.html terupdate)."""
    _, item = ItemService.create_item(title="Item Akan Dihapus")

    response = client.post(
        f"/items/delete/{item.id}",
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "items-list-container" in html
    assert "Item Akan Dihapus" not in html


def test_api_items_endpoint(client, app):
    """Menguji endpoint REST API JSON /api/items."""
    ItemService.create_item(title="API Test Item", description="JSON API")

    response = client.get("/api/items")
    assert response.status_code == 200
    json_data = response.get_json()

    assert json_data["status"] == "success"
    assert json_data["total"] >= 1
    assert json_data["data"][0]["title"] == "API Test Item"
