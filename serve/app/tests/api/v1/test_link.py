from datetime import datetime, timedelta

import pytest
from app.tests.utils.gen_link_short import gen_link_short
from fastapi.testclient import TestClient

API_URL = "/api/v1/link"


def test_create_link_empty_json(client: TestClient):
    response = client.post(f"{API_URL}/")
    assert response.status_code == 422


@pytest.mark.parametrize(
    "link_short, status_code, link_origin, expires_dt",
    [
        ("b", 201, "https://google.com/", "2022-03-24T15:14:39.391Z"),
        ("c", 201, "https://ads.google.com/", "2022-04-25T15:14:39.391Z"),
        ("d", 201, "https://analytics.google.com/", "2022-05-26T15:14:39.391Z"),
        ("e", 201, "https://analytics.google.com/", "2022-06-26T15:14:39.391Z"),
    ],
)
def test_create_link(
    client: TestClient,
    link_short: str,
    status_code: int,
    link_origin: str,
    expires_dt: str,
):
    """Test link creation"""
    payload = {
        "link_origin": link_origin,
        "expires_dt": expires_dt,
    }
    response = client.post(f"{API_URL}/", json=payload)
    assert response.status_code == status_code
    assert "link_short" in response.json()
    assert "id" in response.json()
    assert response.json()["link_short"] == link_short
    assert "expires_dt" in response.json()


@pytest.mark.parametrize(
    "expires_dt, status_code, link_origin",
    [
        ("2203-12-22T00:00", 422, "https://analytics.google.com/"),
        ("11", 422, "https://analytics.google.com/"),
    ],
)
def test_create_link_invalid_dt(
    client: TestClient, expires_dt: str, status_code: int, link_origin: str
):
    payload = {"link_origin": link_origin, "expires_dt": expires_dt}
    response = client.post(f"{API_URL}/", json=payload)
    assert response.status_code == status_code


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
    response = client.get(f"{API_URL}/{link_short}")
    assert response.ok == True
    assert response.json()["link_origin"] == link_origin


@pytest.mark.parametrize(
    "current_link_short, new_link_origin, new_link_short",
    [
        ("b", "https://google.com/", "f54"),
        ("c", "https://ads.google.com/", "rt09"),
        ("d", "https://analytics.google.com/", "Mi7"),
    ],
)
def test_update_link(
    client: TestClient,
    current_link_short: str,
    new_link_origin: str,
    new_link_short: str,
):
    payload = {
        "link_short": new_link_short,
        "link_origin": new_link_origin,
    }
    response = client.put(f"{API_URL}/{current_link_short}", json=payload)
    res_json = response.json()
    assert response.ok == True
    assert res_json["link_short"] == new_link_short
    assert res_json["link_origin"] == new_link_origin


@pytest.mark.parametrize(
    "status, current_link_short, new_link_origin, new_link_short",
    [
        (409, "f54", "https://ads.google.com/", "Mi7"),
        (409, "rt09", "https://analytics.google.com/", "Mi7"),
        (422, "Mi7", "https://analytics.google.com/", "Mi_+7"),
    ],
)
def test_update_link_invalid(
    client: TestClient,
    current_link_short: str,
    new_link_origin: str,
    new_link_short: str,
    status: int,
):
    payload = {
        "link_short": new_link_short,
        "link_origin": new_link_origin,
    }
    response = client.put(f"{API_URL}/{current_link_short}", json=payload)
    assert response.status_code == status


@pytest.mark.parametrize(
    "status, link_short",
    [
        (202, "f54"),
        (202, "Mi7"),
    ],
)
def test_delete_link(client: TestClient, status: int, link_short: str):
    response = client.delete(f"{API_URL}/{link_short}")
    assert response.status_code == status


@pytest.mark.parametrize(
    "status, link_short",
    [
        (404, "f5422"),
        (404, "Mi7dff"),
    ],
)
def test_delete_link_invalid(client: TestClient, status: int, link_short: str):
    response = client.delete(f"{API_URL}/{link_short}")
    assert response.status_code == status
