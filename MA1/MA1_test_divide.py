# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_divide(self):
        print('\nTests divide')
        self.assertEqual(divide(2, 5), 0)
        self.assertEqual(divide(5, 2), 2)
        self.assertEqual(divide(16, 5), 3)
        # self.assertEqual(divide(0, 1), 0) # Optional to handle


if __name__ == "__main__":
    unittest.main()
