import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

# sys.path.append(os.path.abspath(os.path.join('../scripts')))
from scripts.file_handler import FileHandler

class TestFileHandler(unittest.TestCase):


    def setUp(self) -> pd.DataFrame:
        self.file_handle = FileHandler()


    def test_read_csv(self):
        df = self.file_handle.read_csv('data/data.csv')
        df_test = pd.read_csv('data/data.csv')
        self.assertEqual(df.shape, df_test.shape)


if __name__ == '__main__':
    unittest.main()
