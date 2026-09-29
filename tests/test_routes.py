# ==========================================
# Nama File:          test_routes.py
# Deskripsi File:     Pengujian integrasi rute dasar aplikasi Flask
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  28-09-2026
# Tanggal Pembaruan:  29-09-2026
# Catatan:
#   - Menguji halaman beranda mengembalikan status HTTP 200
#   - Menguji endpoint health check
# ==========================================


def test_index_route(client):
    """Menguji render halaman beranda mengembalikan status HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Flask Modern Template" in response.get_data(as_text=True)


def test_health_check_endpoint(client):
    """Menguji endpoint /health mengembalikan status 200 dan data JSON valid."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "Flask-Template-v2" in data["service"]
