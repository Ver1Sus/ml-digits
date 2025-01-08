from app.api.v1.db.protocol import DatabaseInterface
from app.api.v1.schemas.image_schema import PredictionResponse
from functools import wraps
import time


def measure_time(db_client: DatabaseInterface):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            response: PredictionResponse = await func(*args, **kwargs)
            elapsed_time = time.time() - start_time

            # There can be Kafka instead DB
            await db_client.log_request_time(kwargs["data"], response.prediction, elapsed_time)
            return response
        return wrapper
    return decorator
