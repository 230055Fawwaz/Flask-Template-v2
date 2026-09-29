// ==========================================
// Nama File:          script.js
// Deskripsi File:     Skrip pendukung interaktivitas untuk Flask Template v2
// Penulis File:       Fawwaz Yaqzhan & Google Antigravity
// Tanggal Pembuatan:  06-09-2026
// Tanggal Pembaruan:  29-09-2026
// Catatan:
//   - Bekerja secara harmonis bersama HTMX dan Alpine.js
//   - Menangani event lifecycle HTMX global
// ==========================================

document.addEventListener("DOMContentLoaded", () => {
    initHtmxEvents();
});

/**
 * Mengatur interaksi khusus saat event HTMX terjadi
 */
function initHtmxEvents() {
    // Tangani galat respons server dari permintaan HTMX
    document.body.addEventListener("htmx:responseError", (event) => {
        console.error("HTMX Response Error:", event.detail);
    });

    // Tangani galat jaringan atau koneksi terputus saat request HTMX
    document.body.addEventListener("htmx:sendError", (event) => {
        console.error("HTMX Network/Send Error:", event.detail);
    });
}
