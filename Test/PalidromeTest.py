import unittest
from Program.Palinmdrom import checkPalindrom

class PalindromeTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(checkPalindrom("sAN"),True)