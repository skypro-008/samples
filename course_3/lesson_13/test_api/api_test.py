import pytest

from main import app

@pytest.fixture
def test_client():
    return app.test_client()


def test_all_posts_have_correct_keys(test_client):
    result = test_client.get("/")

    assert result.status_code == 200, "Запрошенная страничка не возвращает код 200"

    data = result.json
    assert data["status"] == "ok", "Статус не возвращает 200"

    assert type(data) == dict


