import os
import requests
import random
from typing import List
from sklearn.metrics import accuracy_score
from tkww_api.utils.logger import Log
from tkww_api.utils.utils import load_file


class ModelRetrainer:

    test_data_name = "test-data.p"
    test_labels_name = "test-labels.p"
    data_path = "tkww_api/utils/data/"
    models_path = "tkww_api/utils/models/"

    @classmethod
    def load_test_data_and_labels(cls) -> tuple:
        """Load test data and labels.

        This method loads the test data and labels from the specified data path.

        Returns:
            tuple: A tuple containing the test data and test labels.
        """
        test_data = load_file(cls.data_path, cls.test_data_name)
        test_labels = load_file(cls.data_path, cls.test_labels_name)
        return test_data, test_labels

    @classmethod
    def get_models(cls) -> List[str]:
        """Get the list of model names.

        This method returns a list of model names by scanning the models_path directory
        and filtering the files with a ".p" extension.

        Returns:
            List[str]: A list of model names.
        """
        try:
            files = os.listdir(cls.models_path)
            return [file for file in files if file.endswith(".p")]
        except OSError as e:
            print(f"Error loading model names: {e}")
            return []

    @classmethod
    def select_model(cls, models: List[str]) -> str:
        """Selects a random model from the given list of models.

        Args:
            models (List[str]): A list of model names.

        Returns:
            str: The selected model name.
        """
        if not models:
            print("No models found.")
            return ""
        selected_model = random.choice(models)
        print(f"Selected model: {selected_model}")
        return selected_model

    @classmethod
    def test_model(cls, model_name: str) -> None:
        """Test the specified model using the test data and labels.

        This method loads the model, makes predictions on the test data,
        calculates the accuracy and prints the accuracy of the model.

        Args:
            model_name (str): The name of the model to be tested.
        """
        test_data, test_labels = cls.load_test_data_and_labels()
        model = load_file(cls.models_path, model_name)
        predictions = model.predict(test_data)
        accuracy = accuracy_score(test_labels, predictions)
        print(f"Accuracy: {accuracy}")

    @classmethod
    def load_new_model_to_api(cls, model_name: str) -> None:
        """Load a new model to the API.

        This method sends a POST request to the API to load a new model.
        It takes the model name as input and sends it as JSON data to the API.

        Args:
            model_name (str): The name of the model to be loaded.

        Returns:
            None

        Raises:
            Exception: If there is an error communicating with the API.

        """
        API_URL = "http://18.201.57.160:80/change_model"
        headers = {"Content-Type": "application/json"}
        data = {"model": model_name}

        try:
            response = requests.post(API_URL, json=data, headers=headers)
            if response.status_code == 200:
                print(f"Model {model_name} successfully loaded to API.")
            else:
                print(f"Failed to load model {model_name} to API. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error communicating with API: {e}")

    @classmethod
    def retrain_and_test_model(cls) -> None:
        """Retrains and tests a model.

        This method selects a model from the models directory, loads it, and performs
        a simulation of training, prediction, and metric calculation using test data.
        The accuracy of the model is then printed.

        Returns:
            None
        """
        print("Retraining, testing and loading a new model to the API.\n")
        models = cls.get_models()
        selected_model = cls.select_model(models)
        if selected_model:
            cls.test_model(selected_model)
            cls.load_new_model_to_api(selected_model)


if __name__ == "__main__":
    ModelRetrainer.retrain_and_test_model()
