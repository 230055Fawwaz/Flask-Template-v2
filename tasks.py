# ==========================================
# Nama File:          tasks.py
# Deskripsi File:     Task runner otomasi cross-platform berbasis Invoke
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  28-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Menggantikan kebutuhan file batch script (.bat) spesifik Windows
#   - Berjalan lancar di berbagai sistem operasi (Windows, Linux, macOS)
#   - Menyediakan perintah cepat: run, test, lint, format, check, clean, db
# ==========================================

import os
import shutil
import sys
from pathlib import Path
from invoke import task

# Flag untuk kompatibilitas PTY (hanya aktif di sistem operasi selain Windows)
USE_PTY = sys.platform != "win32"


@task
def run(ctx, host="127.0.0.1", port=5000, debug=True):
    """Menjalankan server development Flask."""
    print(f"[*] Menjalankan Flask Development Server di http://{host}:{port}/ ...")
    cmd = f"{sys.executable} run.py"
    ctx.run(cmd, pty=USE_PTY)


@task
def install(ctx, dev=True):
    """Menginstal paket dependensi proyek."""
    req_file = "requirements-dev.txt" if dev else "requirements.txt"
    print(f"[*] Menginstal dependensi dari {req_file}...")
    ctx.run(f"{sys.executable} -m pip install --upgrade pip", pty=USE_PTY)
    ctx.run(f"{sys.executable} -m pip install -r {req_file}", pty=USE_PTY)
    print("[V] Dependensi berhasil diinstal.")


@task
def lint(ctx):
    """Menjalankan pemeriksaan kualitas kode menggunakan Ruff."""
    print("[*] Menjalankan linter Ruff...")
    ctx.run("ruff check .", pty=USE_PTY)


@task
def format(ctx):
    """Memformat kode dan merapikan import secara otomatis dengan Ruff."""
    print("[*] Memformat kode dengan Ruff...")
    ctx.run("ruff format .", pty=USE_PTY)
    print("[*] Mengurutkan import dan menerapkan perbaikan linter...")
    ctx.run("ruff check --fix .", pty=USE_PTY)
    print("[V] Pemformatan selesai.")


@task
def test(ctx):
    """Menjalankan seluruh automated test suite menggunakan Pytest."""
    print("[*] Menjalankan automated test suite...")
    ctx.run("pytest", pty=USE_PTY)


@task(pre=[lint, test])
def check(ctx):
    """Menjalankan pemeriksaan lengkap (linting + testing)."""
    print("[V] Seluruh pemeriksaan (linting dan testing) lolos.")


@task
def clean(ctx):
    """Membersihkan file cache Python, pytest, dan ruff."""
    print("[*] Membersihkan cache proyek...")
    patterns = [
        "**/__pycache__",
        "**/*.pyc",
        "**/*.pyo",
        "**/.pytest_cache",
        "**/.ruff_cache",
        "**/.coverage",
        "**/htmlcov",
    ]
    base_dir = Path(".")
    removed_count = 0

    for pattern in patterns:
        for path in base_dir.glob(pattern):
            try:
                if path.is_file():
                    path.unlink()
                    removed_count += 1
                elif path.is_dir():
                    shutil.rmtree(path, ignore_errors=True)
                    removed_count += 1
            except OSError:
                pass

    print(f"[V] Berhasil membersihkan {removed_count} file/folder cache.")


# --- GRUP TASK DATABASE (MIGRASI) ---
@task
def db_init(ctx):
    """Inisialisasi repositori migrasi database (hanya pertama kali)."""
    print("[*] Menginisialisasi repositori migrasi Alembic...")
    env = {"FLASK_APP": "run.py"}
    ctx.run("flask db init", env=env, pty=USE_PTY)


@task
def db_migrate(ctx, message="update_schema"):
    """Membuat revisi migrasi database baru berdasarkan perubahan model."""
    print(f"[*] Membuat migrasi baru dengan pesan: '{message}'...")
    env = {"FLASK_APP": "run.py"}
    ctx.run(f'flask db migrate -m "{message}"', env=env, pty=USE_PTY)


@task
def db_upgrade(ctx):
    """Menerapkan seluruh migrasi yang belum dijalankan ke database."""
    print("[*] Menerapkan migrasi ke database...")
    env = {"FLASK_APP": "run.py"}
    ctx.run("flask db upgrade", env=env, pty=USE_PTY)


@task
def db_history(ctx):
    """Melihat riwayat versi migrasi database."""
    env = {"FLASK_APP": "run.py"}
    ctx.run("flask db history", env=env, pty=USE_PTY)
