# ==========================================
# Nama File:          conftest.py
# Deskripsi File:     Konfigurasi dan fixture Pytest untuk pengujian otomatis
# Penulis File:       Fawwaz Yaqzhan & Google Antigravity
# Tanggal Pembuatan:  28-09-2026
# Tanggal Pembaruan:  28-09-2026
# Catatan:
#   - Menyediakan fixture app dan client dengan database SQLite in-memory
#   - Menjamin isolasi data antar pengujian (test isolation)
# ==========================================

import pytest
from app import create_app
from app.config import TestingConfig
from app.extensions import db


@pytest.fixture
def app():
    """Fixture untuk instance aplikasi Flask dengan TestingConfig."""
    test_app = create_app(TestingConfig)

    with test_app.app_context():
        db.create_all()
        yield test_app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Fixture test client untuk simulasi HTTP request."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Fixture CLI runner untuk pengujian perintah terminal Flask."""
    return app.test_cli_runner()
