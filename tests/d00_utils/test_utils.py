import pandas as pd
import numpy as np
import glob
import functools
import pytest
import os
import sys

src_dir = os.path.join(os.getcwd(), '..', '..', 'src')
sys.path.append(src_dir)

from d00_utils.utils import read_multiple_csv_and_concat


class TestReadMultipleCsvAndConcat(object):

    def test_on_concat_no_missing_files(self):

        actual = len(read_multiple_csv_and_concat('file_test_20*/file*'))
        assert actual == 12
