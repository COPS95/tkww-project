import unittest
from fastapi.testclient import TestClient
from tkww_api.controllers.model_controller import router
from tkww_api.services.model_service import ModelService
from tkww_api.envelopes.model_envelope import ChangeModelRequest, PredictionRequest

client = TestClient(router)


class TestModelController(unittest.TestCase):
    def setUp(self):
        """Initialize the test case with a ModelService instance."""
        self.model_service = ModelService()

    def test_index(self):
        """Test the index endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the API"}

    def test_endpoint_predict(self):
        """Test the predict endpoint."""
        self.model_service.predict = lambda self, req: ([], "TestModel")
        request_data = PredictionRequest(sepallength=5.1, sepalwidth=3.5, petallength=1.4, petalwidth=0.2)
        response = client.get("/predict", params=request_data.model_dump())
        assert response.status_code == 200

    def test_endpoint_change_model(self):
        """Test the change_model endpoint."""

        self.model_service.change_model = lambda self, model_name: {"status": "Success"}
        request_data = ChangeModelRequest(model="rf-1.p")
        response = client.post("/change_model", json=request_data.model_dump())
        assert response.status_code == 200
        assert response.json()["status"] == "Success"
