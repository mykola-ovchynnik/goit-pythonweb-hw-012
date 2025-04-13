import pytest
from src.services.users import UserService
from tests.test_helpers import TEST_USER, CONTACT_EXAMPLE, HEADERS_TEMPLATE


@pytest.mark.asyncio
async def test_create_contact(client, db_session):
    await client.post("/auth/register", json=TEST_USER)
    user_service = UserService(db_session)
    await user_service.confirm_email(TEST_USER["email"])
    login = await client.post(
        "/auth/login",
        data={"username": TEST_USER["username"], "password": TEST_USER["password"]},
    )
    token = login.json()["access_token"]

    # Тест створення контакту
    response = await client.post(
        "/contacts/", json=CONTACT_EXAMPLE, headers=HEADERS_TEMPLATE(token)
    )
    assert response.status_code == 200
    assert response.json()["email"] == CONTACT_EXAMPLE["email"]
