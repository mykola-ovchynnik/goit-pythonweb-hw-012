import pytest
from src.services.users import UserService


@pytest.mark.asyncio
async def test_confirm_email_unit(db_session):
    service = UserService(db_session)
    await service.confirm_email("test@example.com")
