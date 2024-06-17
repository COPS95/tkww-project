import unittest
import numpy as np
from tkww_api.services.model_service import ModelService
from tkww_api.envelopes.model_envelope import PredictionRequest


class TestModelService(unittest.TestCase):

    def setUp(self):
        """Initialize the test case with a ModelService instance."""
        self.model_service = ModelService()

    def test_predict(self):
        """Test the predict method of the model service"""
        self.model_service.model = MockModel()
        features = PredictionRequest(sepallength=5.1, sepalwidth=3.5, petallength=1.4, petalwidth=0.2)
        prediction, model_name = self.model_service.predict(features)

        # Assert the result
        self.assertEqual(prediction, [2])
        self.assertEqual(model_name, self.model_service.model_name)

    def test_change_model_success(self):
        """Test changing the model to a valid model."""
        model_name = "rf-1.p"
        result = self.model_service.change_model(model_name)

        # Assert the result
        self.assertEqual(result["status"], "Success")
        self.assertEqual(result["message"], f"Model {model_name} loaded successfully.")
        self.assertEqual(self.model_service.model_name, model_name)

    def test_change_model_not_found(self):
        """Test changing the model to a model that does not exist."""
        model_name = "new_model"
        result = self.model_service.change_model(model_name)

        # Assert the result
        self.assertEqual(result["status"], "Failed")
        self.assertEqual(result["error"], f"Model {model_name} not found.")
        self.assertNotEqual(self.model_service.model_name, model_name)


class MockModel:
    def predict(self, X):
        return np.array([2])


if __name__ == "__main__":
    unittest.main()
