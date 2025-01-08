from fastapi import APIRouter, UploadFile, File
from ..db.sqlite import SqlLiteDatabaseClient
from ..utils.query_time import measure_time

from app.api.v1.schemas.image_schema import ImageRequest, PredictionResponse
from app.api.v1.services import process_image

router = APIRouter()
db_client = SqlLiteDatabaseClient()


@router.post("/predict-image-array/", response_model=PredictionResponse)
@measure_time(db_client)
async def predict_image_array(data: ImageRequest):
    prediction = await process_image.predict_image_array(data)
    return PredictionResponse(prediction=prediction)


@router.get("/predict-image-file/", response_model=PredictionResponse)
@measure_time(db_client)
async def predict_image_file(file: UploadFile = File(...)):
    prediction = await process_image.predict_image_file(file)
    return PredictionResponse(prediction=prediction)
