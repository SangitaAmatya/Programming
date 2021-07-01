import unittest
from Program.ReverseA_String import RevesrseA_String

class PalindromeTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(RevesrseA_String("aditya MAATY"))

    def testcase2(self):
        self.assertEqual(RevesrseA_String([1,23,34,56]))