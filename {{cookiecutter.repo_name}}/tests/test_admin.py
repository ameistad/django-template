import pytest


@pytest.mark.django_db
def test_admin(admin_client):
    """
    Tests whether the admin page sends a 200 HTTP status code as response.
    """
    response = admin_client.get('http://localhost:8000/admin/')
    assert response.status_code == 200
