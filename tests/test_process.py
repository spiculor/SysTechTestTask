import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_basic():
    response = client.post("/process/", json={"text": "Пример текста для обработки."})
    assert response.status_code == 200
    tokens = response.json().get("tokens", [])
    assert tokens == ["пример", "текст", "обработка"]

def test_process_empty():
    response = client.post("/process/", json={"text": ""})
    assert response.status_code == 200
    tokens = response.json().get("tokens", [])
    assert tokens == []  

def test_process_symbols():
    response = client.post("/process/", json={"text": "123! @Тестовый текст$#."})
    assert response.status_code == 200
    tokens = response.json().get("tokens", [])
    assert tokens == ["тестовый", "текст"]
