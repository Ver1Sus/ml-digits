from .protocol import DatabaseInterface
from typing import Optional
import sqlite3

db_file = 'my_database.db'


class SqlLiteDatabaseClient(DatabaseInterface):
    def __init__(self):
        self.conn = sqlite3.connect(
            db_file,
            check_same_thread=False,  # Hack for working in different thread. Need different DB
        )
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY,
                input TEXT,
                prediction INTEGER,
                response_time FLOAT
            )
        ''')
        cursor.close()

    async def log_request_time(self, input: dict, prediction: int, response_time: float):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO predictions (input, prediction, response_time) VALUES (?, ?, ?)',
                       (str(input), prediction, response_time))
        self.conn.commit()
        cursor.close()

    async def get_predictions_count(self, prediction: int) -> int:
        cursor = self.conn.cursor()
        cursor.execute('SELECT count(id) FROM predictions WHERE prediction = ?', (prediction,))
        row = cursor.fetchone()
        cursor.close()
        return row[0]

    async def get_average_prediction_time(self, prediction: int) -> Optional[float]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT avg(response_time) FROM predictions WHERE prediction = ?', (prediction,))
        row = cursor.fetchone()
        cursor.close()
        return row[0]


