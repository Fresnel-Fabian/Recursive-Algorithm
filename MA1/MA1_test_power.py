# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_power(self):
        print('\nTests power')
        self.assertEqual(power(2, 5), 32, "2^5 = 32")
        self.assertEqual(power(2, 0), 1, "2^0 = 1")
        self.assertEqual(power(10, -1), 0.1, "10^-1 = 0.1")


if __name__ == "__main__":
    unittest.main()
