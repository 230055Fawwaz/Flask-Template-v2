// ==========================================
// Nama File:          script.js
// Deskripsi File:     Skrip interaktivitas DOM vanilla untuk template web Flask
// Penulis File:       Fawwaz Yaqzhan & Google Antigravity
// Tanggal Pembuatan:  06-09-2026
// Tanggal Pembaruan:  06-09-2026
// Catatan:
//   - Menangani penutupan notifikasi flash message secara manual dan otomatis
//   - Menyediakan konfirmasi interaktif saat menghapus item data
//   - Mencegah double submit pada formulir penambahan item
// ==========================================

document.addEventListener("DOMContentLoaded", () => {
    initAlerts();
    initDeleteConfirmations();
    initFormProtection();
});

/**
 * Menginisialisasi fungsionalitas alert flash message
 */
function initAlerts() {
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach((alert) => {
        // Tombol tutup manual
        const closeBtn = alert.querySelector(".alert-close");
        if (closeBtn) {
            closeBtn.addEventListener("click", () => {
                dismissAlert(alert);
            });
        }

        // Auto dismiss setelah 5 detik
        setTimeout(() => {
            dismissAlert(alert);
        }, 5000);
    });
}

/**
 * Efek memudarkan alert saat ditutup
 */
function dismissAlert(alertElement) {
    if (!alertElement || alertElement.dataset.dismissing) return;
    alertElement.dataset.dismissing = "true";

    alertElement.style.transition = "opacity 0.3s ease, transform 0.3s ease";
    alertElement.style.opacity = "0";
    alertElement.style.transform = "translateY(-8px)";

    setTimeout(() => {
        alertElement.remove();
    }, 300);
}

/**
 * Menambahkan konfirmasi sebelum menghapus item
 */
function initDeleteConfirmations() {
    const deleteForms = document.querySelectorAll(".delete-form");

    deleteForms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            const confirmed = window.confirm("Apakah Anda yakin ingin menghapus item ini dari database?");
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
}

/**
 * Mencegah pengiriman formulir ganda (double-submission)
 */
function initFormProtection() {
    const createForm = document.getElementById("form-create-item");
    const submitBtn = document.getElementById("btn-submit-item");

    if (createForm && submitBtn) {
        createForm.addEventListener("submit", () => {
            submitBtn.disabled = true;
            submitBtn.textContent = "Menyimpan data...";
            submitBtn.style.opacity = "0.75";
        });
    }
}
