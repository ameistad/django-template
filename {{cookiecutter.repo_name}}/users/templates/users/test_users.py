import pytest


@pytest.mark.django_db
def test_profile(admin_client):
    """
    Tests whether the profile page sends a 200 HTTP status code as response.
    """
    response = admin_client.get('http://localhost:8000/users/testuser')
    assert response.status_code == 200
