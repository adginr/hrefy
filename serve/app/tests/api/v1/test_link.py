import pytest
from fastapi.testclient import TestClient


def test_create_link_empty_json(client: TestClient):
    response = client.post("/api/v1/link/")
    assert response.status_code == 422


@pytest.mark.parametrize(
    "link_short, status_code, link_origin ",
    [
        ("b", 201, "https://google.com/"),
        ("c", 201, "https://ads.google.com/"),
        ("d", 201, "https://analytics.google.com/"),
        ("e", 201, "https://analytics.google.com/"),
    ],
)
def test_create_link_with_dublicant(
    client: TestClient, link_short: str, status_code: int, link_origin: str
):
    """Test link creation"""
    payload = {"link_origin": link_origin}
    response = client.post("/api/v1/link/", json=payload)
    assert response.status_code == status_code
    assert "link_short" in response.json()
    assert "id" in response.json()
    assert response.json()["link_short"] == link_short


@pytest.mark.parametrize(
    "link_short, link_origin",
    [
        ("b", "https://google.com/"),
        ("c", "https://ads.google.com/"),
        ("d", "https://analytics.google.com/"),
    ],
)
def test_read_link(client: TestClient, link_short: str, link_origin: dict[str, str]):
    """Test wheather link exists on get requests"""
    response = client.get(f"/api/v1/link/{link_short}")
    assert response.ok == True
    assert response.json()["link_origin"] == link_origin
