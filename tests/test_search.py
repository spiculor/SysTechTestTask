import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_basic():
    response = client.post("/search/", json={"text": "технологии"})
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert len(results) == 3
    assert "технологии" in results[0].lower() or "технологии" in results[1].lower() or "технологии" in results[2].lower()

def test_search_empty_query():
    response = client.post("/search/", json={"text": ""})
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert len(results) == 0  

def test_search_no_match():
    response = client.post("/search/", json={"text": "несуществующее слово"})
    assert response.status_code == 200
    results = response.json().get("results", [])
    assert len(results) == 0
