# ==========================================
# Nama File:          main_routes.py
# Deskripsi File:     Definisi rute blueprint utama aplikasi dengan dukungan HTMX
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Menghubungkan endpoint HTTP ke fungsi di ItemService
#   - Menerapkan progressive enhancement: respons partial HTML untuk HTMX dan redirect untuk form standar
#   - Menyediakan endpoint REST API JSON
# ==========================================

from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from app.services.item_service import ItemService

# Inisialisasi Blueprint utama
main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    """Menampilkan halaman beranda aplikasi dengan daftar item."""
    items = ItemService.get_all_items()
    return render_template("pages/index.html", items=items)


@main_bp.route("/items/create", methods=["POST"])
def create_item():
    """Endpoint untuk menambahkan item baru melalui formulir."""
    title = request.form.get("title")
    description = request.form.get("description")

    success, result = ItemService.create_item(title=title, description=description)

    if success:
        flash(f"Item '{result.title}' berhasil ditambahkan!", "success")
    else:
        flash(str(result), "error")

    # Respon cepat partial HTML untuk permintaan AJAX dari HTMX
    if request.headers.get("HX-Request"):
        items = ItemService.get_all_items()
        return render_template("components/_item_list.html", items=items)

    return redirect(url_for("main.index"))


@main_bp.route("/items/toggle/<int:item_id>", methods=["POST"])
def toggle_item(item_id):
    """Endpoint untuk mengubah status selesai/belum selesai suatu item."""
    success, result = ItemService.toggle_item_status(item_id)

    if success:
        status_text = "selesai" if result.is_completed else "aktif kembali"
        flash(f"Status item '{result.title}' diubah menjadi {status_text}.", "info")

        # Jika dipanggil via HTMX, cukup perbarui baris item yang berubah
        if request.headers.get("HX-Request"):
            return render_template("components/_item_row.html", item=result)
    else:
        flash(str(result), "error")

    if request.headers.get("HX-Request"):
        items = ItemService.get_all_items()
        return render_template("components/_item_list.html", items=items)

    return redirect(url_for("main.index"))


@main_bp.route("/items/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    """Endpoint untuk menghapus item berdasarkan ID."""
    success, message = ItemService.delete_item(item_id)

    if success:
        flash(message, "success")
    else:
        flash(message, "error")

    # Respon partial HTML untuk permintaan HTMX
    if request.headers.get("HX-Request"):
        items = ItemService.get_all_items()
        return render_template("components/_item_list.html", items=items)

    return redirect(url_for("main.index"))


@main_bp.route("/api/items", methods=["GET"])
def api_get_items():
    """Contoh endpoint API untuk mengembalikan data item dalam format JSON."""
    items = ItemService.get_all_items()
    return jsonify({
        "status": "success",
        "total": len(items),
        "data": [item.to_dict() for item in items]
    })
