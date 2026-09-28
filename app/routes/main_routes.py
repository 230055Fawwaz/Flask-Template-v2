# ==========================================
# Nama File:          main_routes.py
# Deskripsi File:     Definisi rute blueprint utama aplikasi
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Menghubungkan URL endpoint HTTP ke fungsi di ItemController
#   - Menyediakan rute web HTML dan endpoint REST API sederhana
#   - Menerapkan flash message dan redirect untuk interaksi formulir
# ==========================================

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.controllers.item_controller import ItemController

# Inisialisasi Blueprint utama
main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    """Menampilkan halaman beranda aplikasi dengan daftar item."""
    items = ItemController.get_all_items()
    return render_template("index.html", items=items)


@main_bp.route("/items/create", methods=["POST"])
def create_item():
    """Endpoint untuk menambahkan item baru melalui formulir."""
    title = request.form.get("title")
    description = request.form.get("description")

    success, result = ItemController.create_item(title=title, description=description)

    if success:
        flash(f"Item '{result.title}' berhasil ditambahkan!", "success")
    else:
        flash(result, "error")

    return redirect(url_for("main.index"))


@main_bp.route("/items/toggle/<int:item_id>", methods=["POST"])
def toggle_item(item_id):
    """Endpoint untuk mengubah status selesai/belum selesai suatu item."""
    success, result = ItemController.toggle_item_status(item_id)

    if success:
        status_text = "selesai" if result.is_completed else "aktif kembali"
        flash(f"Status item '{result.title}' diubah menjadi {status_text}.", "info")
    else:
        flash(result, "error")

    return redirect(url_for("main.index"))


@main_bp.route("/items/delete/<int:item_id>", methods=["POST"])
def delete_item(item_id):
    """Endpoint untuk menghapus item berdasarkan ID."""
    success, message = ItemController.delete_item(item_id)

    if success:
        flash(message, "success")
    else:
        flash(message, "error")

    return redirect(url_for("main.index"))


@main_bp.route("/api/items", methods=["GET"])
def api_get_items():
    """Contoh endpoint API untuk mengembalikan data item dalam format JSON."""
    items = ItemController.get_all_items()
    return jsonify({
        "status": "success",
        "total": len(items),
        "data": [item.to_dict() for item in items]
    })
