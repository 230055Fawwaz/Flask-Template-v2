@echo off
REM ==========================================
REM Nama File:          run_server.bat
REM Deskripsi File:     Skrip batch untuk menjalankan server Flask di lingkungan Windows
REM Penulis File:       Fawwaz Yaqzhan & Google Antigravity
REM Tanggal Pembuatan:  06-09-2026
REM Tanggal Pembaruan:  06-09-2026
REM Catatan:
REM   - Mendeteksi dan mengaktifkan virtual environment (.venv) jika tersedia
REM   - Menjalankan file run.py dengan konfigurasi development
REM   - Memberikan pesan informatif jika terjadi error
REM ==========================================

echo.
echo =======================================================
echo          Menjalankan Flask Development Server
echo =======================================================
echo.

REM Cek apakah direktori .venv tersedia
if exist ".venv\Scripts\activate.bat" (
    echo [*] Mengaktifkan virtual environment (.venv)...
    call .venv\Scripts\activate.bat
) else (
    echo [!] PERINGATAN: Folder .venv tidak ditemukan.
    echo [*] Menjalankan dengan Python global sistem.
    echo [*] Disarankan menjalankan setup_env.bat terlebih dahulu jika belum install dependensi.
    echo.
)

REM Menjalankan aplikasi
python run.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [X] Server berhenti dengan kode error: %ERRORLEVEL%
    pause
)
