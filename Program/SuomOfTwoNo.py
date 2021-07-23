import unittest


def getSum (n):
    # print("sum of two number is : ", getSum(n))
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n / 10
        print ("sum of two number is : ", getSum (n))
    return sum
class SumOfTwoNoTestcase (unittest.TestCase):
    def testcase1 (self):
        self.assertEqual (getSum (1233), 9)
