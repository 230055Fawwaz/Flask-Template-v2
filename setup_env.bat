@echo off
REM ==========================================
REM Nama File:          setup_env.bat
REM Deskripsi File:     Skrip batch untuk membuat virtual environment dan menginstal dependensi
REM Penulis File:       Fawwaz Yaqzhan & Google Antigravity
REM Tanggal Pembuatan:  06-09-2026
REM Tanggal Pembaruan:  06-09-2026
REM Catatan:
REM   - Memeriksa ketersediaan perintah python pada PATH sistem
REM   - Membuat direktori virtual environment .venv secara otomatis
REM   - Menginstal paket-paket dari requirements.txt ke dalam .venv
REM ==========================================

echo.
echo =======================================================
echo          Setup Virtual Environment Flask Template
echo =======================================================
echo.

REM Cek ketersediaan perintah python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [X] ERROR: Python tidak ditemukan pada PATH sistem Anda!
    echo     Silakan instal Python terlebih dahulu dari https://python.org
    pause
    exit /b 1
)

REM Buat virtual environment jika belum ada
if not exist ".venv" (
    echo [*] Membuat virtual environment baru di folder .venv...
    python -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo [X] Gagal membuat virtual environment.
        pause
        exit /b 1
    )
    echo [V] Virtual environment berhasil dibuat.
) else (
    echo [*] Virtual environment (.venv) sudah ada, melanjutkan...
)

REM Aktifkan environment
echo [*] Mengaktifkan .venv...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo [*] Memperbarui pip ke versi terbaru...
python -m pip install --upgrade pip --quiet

REM Install dependensi
echo [*] Menginstal dependensi dari requirements.txt...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [X] Terjadi kendala saat menginstal requirements.
    pause
    exit /b 1
)

echo.
echo =======================================================
echo [V] SELESAI: Lingkungan Python dan dependensi berhasil disiapkan!
echo     Sekarang Anda dapat menjalankan server dengan: run_server.bat
echo =======================================================
echo.
pause
