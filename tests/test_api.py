from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
DIGIT_0 = [
    [0.0, 0.0, 5.0, 13.0, 9.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 13.0, 15.0, 10.0, 15.0, 5.0, 0.0],
    [0.0, 3.0, 15.0, 2.0, 0.0, 11.0, 8.0, 0.0],
    [0.0, 4.0, 12.0, 0.0, 0.0, 8.0, 8.0, 0.0],
    [0.0, 5.0, 8.0, 0.0, 0.0, 9.0, 8.0, 0.0],
    [0.0, 4.0, 11.0, 0.0, 1.0, 12.0, 7.0, 0.0],
    [0.0, 2.0, 14.0, 5.0, 10.0, 12.0, 0.0, 0.0],
    [0.0, 0.0, 6.0, 13.0, 10.0, 0.0, 0.0, 0.0],
]
INVALID_ARRAY = [
    [0.0, 0.12, 2],
    [77, 4],
    [],
]


def test_process_image_array_v1(change_to_root_directory):
    response = client.post("/v1/images/predict-image-array", json={"array": DIGIT_0})
    assert response.status_code == 200
    assert response.json() == {'prediction': 0}


def test_process_image_array_v1_invalid_input(change_to_root_directory):
    response = client.post("/v1/images/predict-image-array", json={"array": INVALID_ARRAY})
    assert response.status_code == 422
