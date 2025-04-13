import pytest
from src.services.users import UserService


user_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "StrongPass123",
}


@pytest.mark.asyncio
async def test_register_user(client):
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]


@pytest.mark.asyncio
async def test_register_user(client, db_session):
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]

    user_service = UserService(db_session)
    await user_service.confirm_email(user_data["email"])


@pytest.mark.asyncio
async def test_login_user(client):
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    response = await client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
