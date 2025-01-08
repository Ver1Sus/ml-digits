from pydantic import BaseModel, conlist
from typing import Optional


class ImageRequest(BaseModel):
    array: conlist(conlist(float, min_length=8, max_length=8), min_length=8, max_length=8)


class PredictionResponse(BaseModel):
    prediction: Optional[int]
