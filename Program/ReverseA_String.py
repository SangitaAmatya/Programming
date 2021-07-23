#In above code, we call a function to reverse a string,
#which iterates to every element and intelligently join each character
#in the beginning so as to obtain the reversed string.
#s=input("enter string : ")
#print(s[::-1])

# Python code to reverse a string
# using recursion
import unittest


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def RevesrseA_String(string):
    str1 = reverse(string)
    print("String in reverse Order :  ", str1)

    if (string == str1):
        return True
    else:
        return False
class PalindromeTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(RevesrseA_String("this is my car"))

    def testcase1 (self):
        expected = ["rac ym si siht"]
        self.assertEqual (expected, RevesrseA_String ('this is my car'), True)


    def testcase3(self):
        expected=" rac ym si siht"
        self.assertEqual(RevesrseA_String("this is my car"))

    def testcase4(self):
        self.assertEqual(RevesrseA_String([1,23,34,56]))