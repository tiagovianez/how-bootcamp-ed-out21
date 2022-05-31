# import datetime
# from unittest.mock import patch
# from ingestors import DataIngestor
# from writers import DataWriter


# # Subscrevendo um método de um determinada classe
# # Nesse caso estou informando que essa classe não tem mais nenhum objeto definido 
# @patch("ingestors.DataIngestor.__abstractmethod__", set())
# class TestIngestors:
#     def test_checkpoint_filename(self):
#         actual = DataIngestor(
#             writer=DataWriter,
#             coins=["TEST", "HOW"],
#             default_start_date=datetime.date(2021, 6, 21)
#         )._checkpoint_filename
#         expected = "DataIngestor.checkpoint"
#         assert actual == expected