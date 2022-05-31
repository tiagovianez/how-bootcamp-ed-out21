import datetime
from typing import Dict, List
import os


class DataTypeNotSupportedForIngestionException(Exception):
    def __init__(self, data):
        self.data = data
        self.message = f"data type {type(data)} is not supported for ingestion"
        super().__init__(self.message)


class DataWriter:

    def __init__(self, api, coin: str) -> None:
        self.coin = coin
        self.api = api
        self.filename = f"{self.api}/{self.coin}/{datetime.datetime.now()}.json"

    # Toda vez que chamar esse método, ele só irá inserir um dado novo sem subscrever o anterior. 'a' = Append
    def _write_row(self, row: str) -> None:
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'a') as f:
            f.write(row)


    def write(self, data: [List, Dict]):
        if isinstance(data, Dict):
            self._write_row(json.dumps(data) + "\n")
        elif isinstance(data, List):
            for element in data:
                self.write(element)
        else:
            raise DataTypeNotSupportedForIngestionException(data)