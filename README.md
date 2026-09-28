# Flask Modern Monolith Template (v2.0) ⚡

Template boilerplate siap pakai untuk membangun aplikasi web modern berbasis **Python Flask** dengan arsitektur **Clean Architecture / Service Layer**, pola **Application Factory**, **Blueprint Routes**, serta antarmuka dinamis **Modern Monolith (Jinja2 + HTMX + Alpine.js)** yang beroperasi **100% offline** tanpa proses build Node.js/NPM.

Dilengkapi dengan perkakas pengembangan standar industri: **Ruff** (linter & formatter ultra cepat), **Invoke** (otomasi task cross-platform), serta **Pytest** (automated testing suite).

---

## 🌟 Fitur Utama v2.0

- **Application Factory Pattern (`create_app`)**: Memisahkan instansiasi aplikasi dari file eksekusi, memudahkan pengujian unit (testing) dan konfigurasi multi-lingkungan (Development, Testing, Production).
- **Arsitektur Service Layer**:
  - **Model (`app/models/`)**: Skema tabel database ORM menggunakan **SQLAlchemy 2.0** via Flask-SQLAlchemy.
  - **Service (`app/services/`)**: Logika bisnis dan query database terisolasi murni dari protokol HTTP.
  - **Routes (`app/routes/`)**: Modul Blueprint HTTP cerdas yang mendukung respons JSON REST API dan partial HTML HTMX.
  - **View (`app/templates/`, `app/static/`)**: Antarmuka modular (layouts, pages, components) dengan estetika modern dark-slate glassmorphism.
- **Modern Monolith UI (Zero Reload & Full Offline)**:
  - **HTMX v2.0**: Memperbarui DOM secara instan tanpa reload browser (*zero-refresh CRUD*).
  - **Alpine.js v3.14**: Interaktivitas client-side ringan (auto-dismiss notifikasi toast, toggle state).
  - **100% Offline Ready**: Seluruh pustaka JS vendor tersimpan lokal di dalam proyek tanpa ketergantungan CDN/internet.
- **Perkakas Pengembangan Modern**:
  - **Ruff**: Pengganti all-in-one untuk black, flake8, isort, dan pylint yang dikonfigurasi via `pyproject.toml`.
  - **Invoke (`tasks.py`)**: Task runner portabel untuk Windows, Linux, dan macOS.
  - **Pytest (`tests/`)**: Automated test suite siap pakai dengan database SQLite *in-memory*.
- **Database SQLite & Flask-Migrate**: Pelacakan riwayat migrasi Alembic serta flag `AUTO_CREATE_TABLES` yang memisahkan mode dev/testing dari production.

---

## 📂 Struktur Direktori Proyek

```text
Flask-Template-v2/
│
├── app/
│   ├── __init__.py               # Application Factory (create_app)
│   ├── config.py                 # Konfigurasi Dev, Testing, dan Production
│   ├── extensions.py             # Inisialisasi db & migrate (cegah circular import)
│   │
│   ├── models/                   # [M] MODEL: Definisi skema tabel SQLAlchemy 2.0
│   │   ├── __init__.py           # Ekspor entitas model
│   │   └── item_model.py         # Contoh entitas model (Item)
│   │
│   ├── services/                 # [S] SERVICE: Logika bisnis & query database
│   │   ├── __init__.py           # Ekspor kelas service
│   │   └── item_service.py       # Operasi bisnis dan query CRUD Item
│   │
│   ├── controllers/              # [DEPRECATED] Kompatibilitas mundur mengarah ke services
│   │   ├── __init__.py
│   │   └── item_controller.py
│   │
│   ├── routes/                   # [R] ROUTES: Blueprint pemetaan endpoint & HTMX partials
│   │   ├── __init__.py           # Ekspor blueprint
│   │   └── main_routes.py        # Blueprint rute utama & API JSON
│   │
│   ├── templates/                # [V] VIEW: Template Jinja2 Modular
│   │   ├── layouts/
│   │   │   └── base.html         # Master layout, SEO, vendor offline scripts
│   │   ├── pages/
│   │   │   └── index.html        # Halaman beranda
│   │   ├── components/           # Partials untuk HTMX & UI dinamis
│   │   │   ├── _alerts.html      # Flash message toast auto-dismiss Alpine.js
│   │   │   ├── _item_row.html    # Komponen baris item individual
│   │   │   └── _item_list.html   # Wadah daftar item & empty state
│   │   ├── base.html             # Wrapper kompatibilitas mundur
│   │   └── index.html            # Halaman beranda utama
│   │
│   └── static/                   # ASSETS: Gaya & Skrip Statis
│       ├── css/
│       │   └── style.css         # Styling dark-slate, glassmorphism, & transisi HTMX
│       └── js/
│           ├── script.js         # Event listener lifecycle HTMX
│           └── vendor/           # Pustaka frontend 100% lokal offline
│               ├── htmx.min.js   # HTMX 2.0.2
│               └── alpine.min.js # Alpine.js 3.14.1
│
├── tests/                        # AUTOMATED TESTING SUITE
│   ├── __init__.py
│   ├── conftest.py               # Fixture Pytest (app, client, runner)
│   ├── test_services.py          # Unit tests logika bisnis & database
│   └── test_routes.py            # Integration tests HTTP & HTMX partials
│
├── instance/                     # Folder otomatis untuk database SQLite (app.db)
├── pyproject.toml                # Konfigurasi terpusat Ruff, Pytest, dan metadata proyek
├── requirements.txt              # Dependensi runtime / production
├── requirements-dev.txt          # Dependensi development & testing (ruff, invoke, pytest)
├── tasks.py                      # Task runner cross-platform berbasis Invoke
├── run.py                        # Titik masuk eksekusi server Flask
├── .env.example                  # Template variabel lingkungan
├── .gitignore                    # Konfigurasi ignorasi git
│
├── setup_env.bat                 # Shortcut Windows: Buat venv & install dependensi dev
├── run_server.bat                # Shortcut Windows: Jalankan server dev
└── db_migrate.bat                # Shortcut Windows: Menu CLI migrasi database
```

---

## 🚀 Panduan Memulai Cepat

### 1. Setup Virtual Environment & Dependensi

#### Menggunakan Terminal (Cross-Platform):
```bash
# 1. Buat virtual environment
python -m venv .venv

# 2. Aktifkan virtual environment
# Windows (CMD):
.venv\Scripts\activate.bat
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# 3. Instal dependensi pengembangan
pip install -r requirements-dev.txt
```

#### Atau Menggunakan Skrip Windows:
Cukup klik dua kali file `setup_env.bat` di File Explorer.

---

### 2. Menjalankan Server Development

Setelah dependensi terpasang, jalankan perintah:
```bash
invoke run
```
Aplikasi akan aktif di: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

*(Pengguna Windows juga dapat mengklik dua kali `run_server.bat` atau menekan `Ctrl+Shift+B` di VS Code).*

---

## ⚡ Daftar Perintah Otomasi (`tasks.py`)

Gunakan perintah `invoke` untuk seluruh kebutuhan alur kerja:

| Perintah | Deskripsi |
| :--- | :--- |
| `invoke run` | Menjalankan Flask development server dengan auto-reload |
| `invoke lint` | Memeriksa kepatuhan kode dan potensi bug dengan Ruff |
| `invoke format` | Memformat kode dan merapikan urutan import secara otomatis |
| `invoke test` | Menjalankan seluruh unit test dan integration test dengan Pytest |
| `invoke check` | Menjalankan pemeriksaan lengkap (linting + testing) |
| `invoke clean` | Membersihkan folder cache `__pycache__`, `.pytest_cache`, `.ruff_cache` |
| `invoke db-init` | Inisialisasi folder repositori migrasi Alembic (hanya pertama kali) |
| `invoke db-migrate -m "pesan"` | Membuat catatan revisi migrasi database baru |
| `invoke db-upgrade` | Menerapkan migrasi ke database SQLite |
| `invoke db-history` | Melihat riwayat versi migrasi database |

---

## 🗄️ Manajemen Database

Template v2 dilengkapi pengaturan `AUTO_CREATE_TABLES`:
* **Mode Development & Testing**: Tabel otomatis dibuat saat aplikasi dijalankan, sehingga pengembang baru dapat langsung bereksperimen tanpa setup migrasi manual.
* **Mode Production**: Skema dikelola murni dan aman menggunakan perintah migrasi:
  ```bash
  invoke db-migrate -m "pesan_perubahan"
  invoke db-upgrade
  ```

---

## 🛠️ Alur Menambahkan Fitur Baru

Untuk menambahkan modul baru dengan standar arsitektur v2:

1. **Definisikan Model** di `app/models/<fitur>_model.py`:
   ```python
   from app.extensions import db

   class Produk(db.Model):
       __tablename__ = "produk"
       id = db.Column(db.Integer, primary_key=True)
       nama = db.Column(db.String(100), nullable=False)
   ```
2. **Buat Service Layer** di `app/services/<fitur>_service.py`:
   ```python
   from app.extensions import db
   from app.models.produk_model import Produk

   class ProdukService:
       @staticmethod
       def get_all():
           return list(db.session.scalars(db.select(Produk)).all())
   ```
3. **Buat Route Blueprint** di `app/routes/<fitur>_routes.py`:
   ```python
   from flask import Blueprint, render_template, request
   from app.services.produk_service import ProdukService

   produk_bp = Blueprint("produk", __name__, url_prefix="/produk")

   @produk_bp.route("/")
   def index():
       data = ProdukService.get_all()
       if request.headers.get("HX-Request"):
           return render_template("components/_produk_list.html", produk=data)
       return render_template("pages/produk.html", produk=data)
   ```
4. **Daftarkan Blueprint** di `app/__init__.py`:
   ```python
   app.register_blueprint(produk_bp)
   ```
5. **Tambahkan Pengujian** di `tests/test_<fitur>.py`.

---

## 👨‍💻 Standar Header File

Setiap berkas kode dilengkapi metadata kepenulisan yang seragam:

```text
Nama File:          <nama_file>
Deskripsi File:     <deskripsi_singkat>
Penulis File:       Fawwaz Yaqzhan & Google Antigravity
Tanggal Pembuatan:  06-09-2026
Tanggal Pembaruan:  28-09-2026
Catatan:
  - <butir_tugas_modul>
```

---

## 📄 Lisensi

Proyek ini bersifat open-source dan bebas digunakan sebagai fondasi proyek web Python Flask skala pemula hingga enterprise.
