import unittest
from Program.Primenumber import checkPrime

class PrimeTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(checkPrime(1),False)
    def testcase2(self):
        self.assertEqual(checkPrime(2),True)
    def testcase3(self):
        self.assertEqual(checkPrime(3),True)
    def testcase4(self):
        self.assertEqual(checkPrime(4),False)
    def testcase5(self):
        self.assertEqual(checkPrime(15),False)
