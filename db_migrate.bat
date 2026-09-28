@echo off
REM ==========================================
REM Nama File:          db_migrate.bat
REM Deskripsi File:     Skrip batch interaktif untuk mengelola migrasi database Flask-Migrate
REM Penulis File:       Fawwaz Yaqzhan & Google Antigravity
REM Tanggal Pembuatan:  06-09-2026
REM Tanggal Pembaruan:  06-09-2026
REM Catatan:
REM   - Mengaktifkan .venv secara otomatis sebelum menjalankan perintah flask
REM   - Menyediakan menu praktis untuk db init, db migrate, dan db upgrade
REM   - Memudahkan tracking skema tabel SQLite tanpa perlu menghafal CLI
REM ==========================================

echo.
echo =======================================================
echo          Manajer Migrasi Database (Flask-Migrate)
echo =======================================================
echo.

REM Aktifkan virtual environment jika ada
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

set FLASK_APP=run.py

:menu
echo Pilih operasi migrasi yang ingin dijalankan:
echo  [1] Inisialisasi Migrasi (flask db init) - Hanya untuk pertama kali
echo  [2] Buat Catatan Migrasi Baru (flask db migrate)
echo  [3] Terapkan Migrasi ke Database (flask db upgrade)
echo  [4] Lihat Riwayat Migrasi (flask db history)
echo  [5] Keluar
echo.
set /p choice="Masukkan nomor pilihan [1-5]: "

if "%choice%"=="1" goto init_db
if "%choice%"=="2" goto migrate_db
if "%choice%"=="3" goto upgrade_db
if "%choice%"=="4" goto history_db
if "%choice%"=="5" goto exit_script

echo [!] Pilihan tidak valid, silakan coba lagi.
echo.
goto menu

:init_db
echo.
echo [*] Menjalankan: flask db init
flask db init
echo.
pause
goto menu

:migrate_db
echo.
set /p msg="Masukkan pesan migrasi (contoh: buat_tabel_items): "
if "%msg%"=="" set msg=update_skema_database
echo [*] Menjalankan: flask db migrate -m "%msg%"
flask db migrate -m "%msg%"
echo.
pause
goto menu

:upgrade_db
echo.
echo [*] Menjalankan: flask db upgrade
flask db upgrade
echo.
pause
goto menu

:history_db
echo.
echo [*] Menjalankan: flask db history
flask db history
echo.
pause
goto menu

:exit_script
echo.
echo Selesai.
