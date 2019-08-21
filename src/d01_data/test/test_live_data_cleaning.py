import pytest

from d01_data.live_data_cleaning import _creat_empty_dataframe

class TestCreatEmptyDataframe(object):

    def test_on_create_empty_dataframe(self):

        actual = len(_creat_empty_dataframe(['test', 'columns'], 20))
        expected = 20
        assert actual == expected
