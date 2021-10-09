import unittest

import Task1

class Test(unittest.TestCase):
    def test_found_file(self):
        with self.assertRaises(FileNotFoundError):
            Task1.FalseOpen("false_file.txt", "r")

    def test_mod(self):
        with self.assertRaises(ValueError):
            Task1.FalseOpen("test.txt", "o")


if __name__ == "__main__":
    unittest.main()