from .protocol import DatabaseInterface
from typing import Optional


class DummyDatabaseClient(DatabaseInterface):
    def __init__(self):
        self.name = "DatabaseClient"

    async def log_request_time(self, input: dict, prediction: int, response_time: float):
        print(f"Logged time for {input}: {response_time:.6f} seconds, prediction {prediction}")

    async def get_predictions_count(self, prediction: int) -> int:
        print("Prediction: ", prediction)
        return prediction

    async def get_average_prediction_time(self, prediction: int) -> Optional[float]:
        print("Prediction: ", prediction)
        return prediction
