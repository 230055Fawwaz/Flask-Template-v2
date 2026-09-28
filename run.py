# ==========================================
# Nama File:          run.py
# Deskripsi File:     Titik masuk (entry point) utama untuk menjalankan server Flask
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  06-09-2026
# Tanggal Pembaruan:  06-09-2026
# Catatan:
#   - Menginstansiasi aplikasi menggunakan Application Factory create_app()
#   - Menjalankan development server pada port default 5000
#   - Menangani debug mode dan hot-reloader
# ==========================================

import os
from app import create_app

# Buat instance aplikasi Flask
app = create_app()

if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")

    print(f"🚀 Memulai server Flask di http://{host}:{port}")
    app.run(host=host, port=port, debug=debug)
