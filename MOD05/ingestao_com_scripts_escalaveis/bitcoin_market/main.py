import datetime
from timeit import repeat
from ingestors import DaySummaryIngestor
from writers import DataWriter
from schedule import every, run_pending, repeat
import time


if __name__ == "__main__":
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter,
        coins=["BTC", "ETH", "LTC", "BCH"],
        default_start_date=datetime.date(2021, 6, 1)
    )


    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()


    while True:
        run_pending()
        time.sleep(0.5)
