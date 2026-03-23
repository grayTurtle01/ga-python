"""
This is the file for the unittest
"""
import unittest
from zandbox import fizz_buzz


class FizzBuzzTests(unittest.TestCase):
    """This the class for unittest"""
    def test_1(self):
        """fizz_buzz(3) --> fizz"""
        self.assertEqual(fizz_buzz(3), "fizz")

    def test_2(self):
        """fizz_buzz(5) --> buzz"""
        self.assertEqual(fizz_buzz(5), "buzz")

    def test_3(self):
        """fizz_buzz(15) --> fizz_buzz"""
        self.assertEqual(fizz_buzz(15), "fizz_buzz")


## unitests only for pytest
def test_4():
    """x"""
    assert fizz_buzz(1) == 1


def test_5():
    """y"""
    assert fizz_buzz(10) == "buzz"


def test_6():
    """z"""
    assert fizz_buzz(7) == 7


if __name__ == "__main__":
    unittest.main()
