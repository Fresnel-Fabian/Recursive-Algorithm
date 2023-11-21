# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_digit_sum(self):
        print('\nTests sum_of_digits')
        print('Decimal digits')
        self.assertEqual(digit_sum(125), 8, "digit_sum(125) = 8")
        self.assertEqual(digit_sum(0), 0, "digit_sum(0) = 0")
        print('OK\nBinary digits')
        self.assertEqual(digit_sum(15, 2), 4, "digit_sum(15,2) = 4")
        self.assertEqual(digit_sum(16, 2), 1, "digit_sum(16,2) = 1")
        print('OK\nHexadecimal digits')
        self.assertEqual(digit_sum(32, 16), 2, "digit_sum(32,2) = 2")
        self.assertEqual(digit_sum(63, 16), 18, "digit_sum(63,2) = 18")
        print('OK\nSeptimal digits')
        self.assertEqual(digit_sum(15, 7), 3)
        print('OK')      

if __name__ == "__main__":
    unittest.main()
