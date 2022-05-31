from datetime import datetime
from bitcoin_market.apis import DaySummaryApi

class TestDaySummaryApi:
    def test_get_data(self):
        actual = DaySummaryApi(coin="BTC").get_data(date=datetime.date(2021, 1, 1))
        expected = ""
        print("actual")
        assert actual == expected