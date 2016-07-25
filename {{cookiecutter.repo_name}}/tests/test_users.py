import pytest


@pytest.mark.django_db
def test_admin(admin_client):
    """
    Tests whether the profile page sends a 200 HTTP status code as response
    when logged in as admin.
    """
    response = admin_client.get('http://localhost:8000/users/admin/')
    assert response.status_code == 200
