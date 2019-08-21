# import pandas as pd
# import numpy as np
# import glob
# import functools
# import pytest

# src_dir = os.path.join(os.getcwd(), '..', '..', 'src')
# sys.path.append(src_dir)

from d00_utils.utils import read_multiple_csv_and_concat

class TestReadMultipleCsvAndConcat(object):

    def test_on_concat_no_missing_files(self):

        actual = len(read_multiple_csv_and_concat('file_test_20*/file*'))
        expected = 12
        assert actual == expected

# class Testldldldld(object):
#
#     def test_on_add_one_to_one(self):
#         actual = add_one_to_one(1)
#         expected = 2
#         assert actual == expected
