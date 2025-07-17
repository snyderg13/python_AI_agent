import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_calc_dir(self):
        result = get_files_info("calculator", ".")
    
    def test_funcs_dir(self):
        result = get_files_info("functions", ".")

if __name__ == "__main__":
    unittest.main()