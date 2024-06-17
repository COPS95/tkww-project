import numpy as np
from typing import Dict, Tuple
from tkww_api.utils.logger import Log
from tkww_api.utils.utils import load_file
from tkww_api.envelopes.model_envelope import PredictionRequest


class ModelService:

    def __init__(self):
        """Initialize the ModelService class.

        This method sets the initial values for the ModelService class.
        It initializes the models path, model name, and loads the model.
        """

        self.models_path = "tkww_api/utils/models/"
        self.model_name = "rf-1.p"
        self.model = load_file(self.models_path, self.model_name)

    def predict(self, features: PredictionRequest) -> Tuple[str, str]:
        """Make a prediction based on the given features.

        This method makes a prediction based on the given features using the current model.

        Args:
            features (PredictionRequest): An instance of the PredictionRequest class containing the input features.

        Returns:
            Tuple[str, str]: A tuple containing the prediction as a list and the model name as a string.
        """

        feature_values = [value for value in vars(features).values()]
        input_data = np.array([feature_values], dtype=np.float32)

        prediction = self.model.predict(input_data)

        return prediction.tolist(), self.model_name

    def change_model(self, model_name: str) -> Dict[str, str]:
        """Change the current model to the specified model.

        Args:
            model_name (str): The name of the model to change to.

        Returns:
            dict: A dictionary containing the status and message of the operation.
        """
        Log.info(f"Changing model to {model_name}")
        try:
            new_model = load_file(self.models_path, model_name)
            print(new_model)
            if new_model is None:
                return {"status": "Failed", "error": f"Model {model_name} not found."}

            self.model_name = model_name
            self.model = new_model
            return {"status": "Success", "message": f"Model {model_name} loaded successfully."}
        except Exception as e:
            Log.error(f"Error changing model: {e}")
            return {"status": "Failed", "error": str(e)}
