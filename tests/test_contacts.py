import pytest
from datetime import date

@pytest.mark.asyncio
async def test_create_contact(client):
    login = await client.post("/auth/login", data={"username": "testuser", "password": "StrongPass123"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    contact = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane@example.com",
        "phone_number": "1234567890",
        "birthday": str(date.today()),
        "additional_info": "Friend from school"
    }
    response = await client.post("/contacts/", json=contact, headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == contact["email"]
