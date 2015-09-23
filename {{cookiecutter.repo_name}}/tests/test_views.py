import pytest


@pytest.mark.django_db
def test_startpage(client):
    """
    Tests whether the base url page sends a 200 HTTP status code as response.
    """
    response = client.get('http://localhost:8000/')
    assert response.status_code == 200