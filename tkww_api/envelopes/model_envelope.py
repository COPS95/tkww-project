from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """This class represents the prediction request.

    Args:
        BaseModel (type): The base model class.
    """

    sepallength: float
    sepalwidth: float
    petallength: float
    petalwidth: float


class PredictionOut(BaseModel):
    """This class represents the prediction output.

    Args:
        BaseModel (type): The base model class.
    """

    prediction: list
    model: str


class ChangeModelRequest(BaseModel):
    """This class represents the request to change the model.

    Args:
        BaseModel (type): The base model class.
    """

    model: str
