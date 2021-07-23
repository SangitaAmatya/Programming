import unittest


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class testfactorial(unittest.TestCase):
    def test_fac(self):
        self.assertEqual(factorial(4),24)

    def test_fac1(self):
        self.assertEqual(factorial(3),6,False)

