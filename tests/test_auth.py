import pytest
from src.services.users import UserService
from tests.test_helpers import TEST_USER, HEADERS_TEMPLATE


async def register_and_login_user(client, db_session, user_data=TEST_USER):
    # Реєстрація
    await client.post("/auth/register", json=user_data)

    # Підтвердження email
    user_service = UserService(db_session)
    await user_service.confirm_email(user_data["email"])

    # Логін
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    response = await client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.mark.asyncio
async def test_register_user(client, db_session):
    response = await client.post("/auth/register", json=TEST_USER)
    assert response.status_code == 201
    assert response.json()["username"] == TEST_USER["username"]

    user_service = UserService(db_session)
    await user_service.confirm_email(TEST_USER["email"])


@pytest.mark.asyncio
async def test_login_user(client, db_session):
    token = await register_and_login_user(client, db_session)
    assert token


@pytest.mark.asyncio
async def test_get_current_user(client, db_session):
    token = await register_and_login_user(client, db_session)
    response = await client.get("/users/me", headers=HEADERS_TEMPLATE(token))
    assert response.status_code == 200
    assert response.json()["username"] == TEST_USER["username"]
