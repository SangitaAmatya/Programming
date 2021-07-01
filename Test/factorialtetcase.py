import unittest
from Program.Factorila import factorial
from Program.Factorila import findevenodd

class testfactorial(unittest.TestCase):
    def test_fac(self):
        self.assertEqual(factorial(0),24)

    def test_fac1(self):
        self.assertEqual(factorial(7),5040)

    def test_even(self):
        self.assertEqual(findevenodd(5),"ODD")