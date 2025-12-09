import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "title": "Check 1 2",
            "description": "this is a test",
            "status": "open",
            "due_date": "2026-01-01 00:00:00.000000"
        }
        response = await ac.post("/tasks/", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Check 1 2"
