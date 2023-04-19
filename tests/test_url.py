import pytest
import server

client = server.app.test_client()


def test_if_index_is_online():
    response = client.get("/")
    assert response.status_code == 200


def test_if_clubs_overview_is_online():
    response = client.get("clubs_overview")
    assert response.status_code == 200
