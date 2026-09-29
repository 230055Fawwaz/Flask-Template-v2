# ==========================================
# Nama File:          main_routes.py
# Deskripsi File:     Definisi rute blueprint utama aplikasi
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  29-09-2026
# Catatan:
#   - Menyediakan rute beranda (index) dan health check
#   - Siap dikembangkan dengan rute aplikasi baru
# ==========================================

from flask import Blueprint, jsonify, render_template

# Inisialisasi Blueprint utama
main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    """Menampilkan halaman beranda starter template."""
    return render_template("pages/index.html")


@main_bp.route("/health", methods=["GET"])
def health_check():
    """Endpoint health check sederhana untuk monitoring status aplikasi."""
    return jsonify(
        {
            "status": "healthy",
            "service": "Flask-Template-v2",
            "message": "Aplikasi Flask berjalan normal dan siap digunakan.",
        }
    )
