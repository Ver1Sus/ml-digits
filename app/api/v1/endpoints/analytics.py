from fastapi import APIRouter
from ..db.sqlite import SqlLiteDatabaseClient
from typing import Optional

router = APIRouter()
db_client = SqlLiteDatabaseClient()


@router.get("/get-predictions-count/", response_model=int)
async def get_predictions_count(prediction: int):
    res = await db_client.get_predictions_count(prediction)
    return res


@router.get("/get-average-prediction-time/", response_model=Optional[float])
async def get_average_prediction_time(prediction: int):
    res = await db_client.get_average_prediction_time(prediction)
    return res
