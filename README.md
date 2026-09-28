# Flask MVC Template Repository ⚡

Template boilerplate siap pakai untuk membangun aplikasi web berbasis **Python Flask** dengan arsitektur **Model-View-Controller (MVC)**, pola **Application Factory**, **Blueprint**, pencegahan **Circular Import**, serta frontend **Vanilla Web** (HTML, CSS, JS) berpenampilan modern dan otomasi **Batch Files** untuk Windows.

---

## 🌟 Fitur Utama

- **Application Factory Pattern (`create_app`)**: Memisahkan instansiasi aplikasi dari file eksekusi, memudahkan pengujian unit (testing) dan konfigurasi multi-lingkungan (Development, Testing, Production).
- **Arsitektur Model-View-Controller (MVC)**:
  - **Model (`app/models/`)**: Skema tabel database ORM menggunakan **Flask-SQLAlchemy**.
  - **View (`app/templates/`, `app/static/`)**: Antarmuka responsif berbasis HTML5, CSS kustom bertema modern, dan Vanilla JavaScript.
  - **Controller (`app/controllers/`)**: Logika bisnis dan query database terisolasi rapi dari layer routing.
  - **Routes (`app/routes/`)**: Modul Blueprint HTTP yang murni memetakan URL ke fungsi controller.
- **Pencegahan Circular Import**: Inisialisasi ekstensi pihak ketiga (`db`, `migrate`) dipusatkan di `app/extensions.py` tanpa mengikat instance `app` secara prematur.
- **Prinsip Single Responsibility (SRP)**: Setiap file memiliki satu tugas spesifik dan terfokus.
- **Database SQLite & Flask-Migrate**: Siap pakai dengan database file lokal SQLite (`instance/app.db`) serta integrasi Alembic untuk tracking skema.
- **Otomasi Skrip Batch Windows**:
  - `setup_env.bat`: Pembuatan virtual environment `.venv` & instalasi dependensi otomatis.
  - `run_server.bat`: Deteksi venv dan eksekusi server development.
  - `db_migrate.bat`: Menu interaktif CLI migrasi database.
- **Standar Header Komentar Terintegrasi**: Seluruh file dilengkapi metadata kepenulisan dan dokumentasi modul.

---

## 📂 Struktur Direktori Proyek

```text
Flask-Template/
│
├── app/
│   ├── __init__.py               # Application Factory (create_app)
│   ├── config.py                 # Konfigurasi aplikasi (Dev, Test, Prod)
│   ├── extensions.py             # Inisialisasi db & migrate (mencegah circular import)
│   │
│   ├── models/                   # [M] MODEL: Definisi skema tabel database
│   │   ├── __init__.py           # Ekspor seluruh entitas model
│   │   └── item_model.py         # Contoh entitas model (Item)
│   │
│   ├── controllers/              # [C] CONTROLLER: Logika bisnis & manipulasi data
│   │   ├── __init__.py           # Ekspor kelas controller
│   │   └── item_controller.py    # Handler data dan operasi CRUD Item
│   │
│   ├── routes/                   # [R] ROUTES: Blueprint pemetaan HTTP endpoint
│   │   ├── __init__.py           # Ekspor blueprint
│   │   └── main_routes.py        # Blueprint rute utama & API JSON
│   │
│   ├── templates/                # [V] VIEW: Antarmuka pengguna HTML (Jinja2)
│   │   ├── base.html             # Master layout, SEO, Google Fonts, Flash alerts
│   │   └── index.html            # Halaman beranda & demo interaktif CRUD
│   │
│   └── static/                   # ASSETS: Tampilan & Interaktivitas
│       ├── css/
│       │   └── style.css         # Styling modern dark-slate, glassmorphism
│       └── js/
│           └── script.js         # Interaksi DOM, auto-dismiss alert, proteksi submit
│
├── instance/                     # Folder otomatis untuk database SQLite (app.db)
├── requirements.txt              # Daftar dependensi Python
├── run.py                        # Titik masuk eksekusi server Flask
├── .env.example                  # Template variabel lingkungan
├── .gitignore                    # Konfigurasi ignorasi git (venv, instance, cache)
│
├── run_server.bat                # Batch script: Menjalankan server Flask
├── setup_env.bat                 # Batch script: Setup venv & install dependensi
└── db_migrate.bat                # Batch script: Menu manajemen migrasi database
```

---

## 🚀 Panduan Memulai Cepat

### Cara 1: Menggunakan Skrip Batch (Direkomendasikan di Windows)

1. **Jalankan Setup Lingkungan**:
   Klik dua kali file `setup_env.bat` atau jalankan lewat terminal:
   ```cmd
   setup_env.bat
   ```
   Skrip ini akan otomatis membuat folder `.venv` dan menginstal seluruh paket dari `requirements.txt`.

2. **Jalankan Server Development**:
   Klik dua kali file `run_server.bat` atau jalankan lewat terminal:
   ```cmd
   run_server.bat
   ```
   Aplikasi akan berjalan di: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### Cara 2: Manual Lewat Terminal / Command Prompt

1. **Buat & Aktifkan Virtual Environment**:
   ```bash
   python -m venv .venv
   # Windows (CMD):
   .venv\Scripts\activate.bat
   # Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # Linux / macOS:
   source .venv/bin/activate
   ```

2. **Instal Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Server**:
   ```bash
   python run.py
   ```

---

## 🗄️ Manajemen Migrasi Database

Template ini mendukung pelacakan perubahan skema database menggunakan **Flask-Migrate**:

### Menggunakan Skrip Praktis:
Jalankan `db_migrate.bat` lalu pilih menu yang diinginkan:
- `[1]` Inisialisasi migrasi pertama kali (`flask db init`).
- `[2]` Membuat file migrasi baru setelah mengubah model (`flask db migrate`).
- `[3]` Menerapkan perubahan ke database SQLite (`flask db upgrade`).

### Manual via Terminal:
```bash
flask db init
flask db migrate -m "inisialisasi_tabel"
flask db upgrade
```

---

## 🛠️ Alur Menambahkan Fitur Baru (Pola MVC)

Untuk menambahkan modul atau fitur baru secara rapi dan mengikuti prinsip Single Responsibility:

1. **Buat Model Data** di `app/models/<fitur>_model.py`:
   ```python
   from app.extensions import db

   class Produk(db.Model):
       __tablename__ = "produk"
       id = db.Column(db.Integer, primary_key=True)
       nama = db.Column(db.String(100), nullable=False)
   ```
   Daftarkan model di `app/models/__init__.py`.

2. **Buat Controller Logika** di `app/controllers/<fitur>_controller.py`:
   ```python
   from app.extensions import db
   from app.models import Produk

   class ProdukController:
       @staticmethod
       def ambil_semua():
           return Produk.query.all()
   ```

3. **Buat Blueprint Rute** di `app/routes/<fitur>_routes.py`:
   ```python
   from flask import Blueprint, render_template
   from app.controllers.produk_controller import ProdukController

   produk_bp = Blueprint("produk", __name__, url_prefix="/produk")

   @produk_bp.route("/")
   def daftar():
       data = ProdukController.ambil_semua()
       return render_template("produk/daftar.html", data=data)
   ```

4. **Daftarkan Blueprint** di `app/__init__.py`:
   ```python
   from app.routes.produk_routes import produk_bp
   app.register_blueprint(produk_bp)
   ```

5. **Buat Tampilan Template** di `app/templates/<fitur>/daftar.html`.

---

## 👨‍💻 Standar Header File

Setiap file di dalam proyek ini menerapkan standar header komentar:

```text
Nama File:          <nama_file>
Deskripsi File:     <deskripsi_singkat>
Penulis File:       Fawwaz Yaqzhan & Google Antigravity
Tanggal Pembuatan:  06-09-2026
Tanggal Pembaruan:  06-09-2026
Catatan:
  - <butir_catatan_tugas>
```

---

## 📄 Lisensi

Proyek ini bersifat open-source dan bebas digunakan sebagai cetak biru (*boilerplate template*) untuk proyek pengembangan aplikasi web Anda.
