from typing import Dict
from fastapi import APIRouter, Depends, HTTPException
from tkww_api.services.model_service import ModelService
from tkww_api.envelopes.model_envelope import ChangeModelRequest, PredictionOut, PredictionRequest
from tkww_api.utils.logger import Log


router = APIRouter()
model_service = ModelService()


@router.get("/")
async def index() -> Dict:
    """
    This function is the handler for the root endpoint.

    Returns:
        Dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome to the API"}


@router.get("/predict", response_model=PredictionOut)
async def predict(request: PredictionRequest = Depends()) -> PredictionOut:
    """Endpoint to make a prediction.

    This endpoint takes a PredictionRequest object as input and returns a PredictionOut object as output.

    Args:
        request (PredictionRequest, optional): The prediction request object containing the input features. Defaults to Depends().

    Returns:
        PredictionOut: The prediction result along with the name of the model used.
    """
    try:
        prediction, model_name = model_service.predict(request)
        return {"prediction": prediction, "model": model_name}

    except Exception as e:
        Log.error(f"Error predicting: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/change_model")
async def change_model(request: ChangeModelRequest) -> Dict:
    """Change the model.

    This function is responsible for changing the model based on the provided request.

    Args:
        request (ChangeModelRequest): The request object containing the model to be changed.

    Returns:
        dict: A dictionary containing the result of the model change operation.
    """
    try:
        result = model_service.change_model(request.model)
        if result["status"] == "Failed":
            Log.error(result["error"])
            raise HTTPException(status_code=500, detail=result["error"])
        return result
    except Exception as e:
        Log.error(f"Model change error: {e}")
        raise HTTPException(status_code=500, detail=f"Model change error: {str(e)}")
