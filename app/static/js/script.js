// ==========================================
// Nama File:          script.js
// Deskripsi File:     Skrip pendukung interaktivitas untuk Flask Template v2
// Penulis File:       Fawwaz Yaqzhan & Google Antigravity
// Tanggal Pembuatan:  06-09-2026
// Tanggal Pembaruan:  28-09-2026
// Catatan:
//   - Bekerja secara harmonis bersama HTMX dan Alpine.js
//   - Menangani event lifecycle HTMX (reset status form & fokus input)
//   - Menyediakan fallback untuk browser tanpa JavaScript modern
// ==========================================

document.addEventListener("DOMContentLoaded", () => {
    initHtmxEvents();
});

/**
 * Mengatur interaksi khusus saat event HTMX terjadi
 */
function initHtmxEvents() {
    const createForm = document.getElementById("form-create-item");
    const titleInput = document.getElementById("input-title");

    // Fokus kembali ke input judul setelah item berhasil ditambahkan via HTMX
    if (createForm) {
        createForm.addEventListener("htmx:afterOnLoad", (event) => {
            if (event.detail.successful && titleInput) {
                titleInput.focus();
            }
        });
    }

    // Tangani galat jaringan HTMX jika terjadi kendala server
    document.body.addEventListener("htmx:responseError", (event) => {
        console.error("HTMX Response Error:", event.detail);
    });

    document.body.addEventListener("htmx:sendError", (event) => {
        console.error("HTMX Network/Send Error:", event.detail);
    });
}
