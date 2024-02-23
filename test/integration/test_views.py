from flask import json
from views import app


def test_get_users_endpoint() -> None:
    client = app.test_client()
    actual = client.get('/users')
    assert actual.status_code == 200


def test_get_user_endpoint() -> None:
    client = app.test_client()
    actual = client.get('/users/1')
    assert actual.status_code in [200, 404]


def test_create_user_endpoint() -> None:
    client = app.test_client()
    user_data = {"id": 1, "name": "Jan"}
    response = client.post('/users', json=user_data)
    assert response.status_code == 201


def test_change_user_data_endpoint() -> None:
    client = app.test_client()
    user_data = {"name": "Jan"}
    response = client.patch('/users/1', json=user_data)
    assert response.status_code in [200, 404]


def test_delete_user_endpoint() -> None:
    client = app.test_client()
    response = client.delete('/users/1')
    assert response.status_code == 204
