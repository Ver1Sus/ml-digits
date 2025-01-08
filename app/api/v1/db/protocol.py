from abc import ABC, abstractmethod
from typing import Optional


class DatabaseInterface(ABC):
    @abstractmethod
    async def log_request_time(self, input: dict, prediction: int, response_time: float):
        pass

    @abstractmethod
    async def get_predictions_count(self, prediction: int) -> int:
        pass

    @abstractmethod
    async def get_average_prediction_time(self, prediction: int) -> Optional[float]:
        pass
