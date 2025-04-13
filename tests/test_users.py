import pytest


@pytest.mark.asyncio
async def test_get_current_user(client):
    login_data = {"username": "testuser", "password": "StrongPass123"}
    login = await client.post("/auth/login", data=login_data)
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get("/users/me", headers=headers)

    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_user_me_with_real_redis(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = await client.get("/users/me", headers=headers)
    assert response.status_code == 200
