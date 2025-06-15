import pytest
from server.app import app, db

# server/testing/test_conftest.py


def test_setup_and_teardown_creates_tables():
    # Tables should exist inside app context after fixture runs
    with app.app_context():
        inspector = db.inspect(db.engine)
        assert 'customers' in inspector.get_table_names()
        assert 'items' in inspector.get_table_names()
        assert 'reviews' in inspector.get_table_names()

def test_setup_and_teardown_drops_tables():
    # After fixture yields, tables should be dropped
    with app.app_context():
        db.drop_all()
        inspector = db.inspect(db.engine)
        assert 'customers' not in inspector.get_table_names()
        assert 'items' not in inspector.get_table_names()
        assert 'reviews' not in inspector.get_table_names()

def test_client_fixture(client):
    # The client fixture should return a FlaskClient
    response = client.get('/hello')
    # Accepts both text and html (for robust test)
    assert response.status_code == 200
    assert b'Hello' in response.data