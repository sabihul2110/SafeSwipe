from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_list_samples():
    response = client.get("/samples")
    assert response.status_code == 200
    samples = response.json()
    assert len(samples) > 0
    assert "sample_id" in samples[0]


def test_predict_valid_sample():
    response = client.post("/samples/1/predict")
    assert response.status_code == 200
    data = response.json()
    assert "predicted_fraud" in data
    assert "fraud_probability" in data
    assert 0 <= data["fraud_probability"] <= 1


def test_predict_invalid_sample():
    response = client.post("/samples/9999/predict")
    assert response.status_code == 404
