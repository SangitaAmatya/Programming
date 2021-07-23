import unittest


def sumofArray (arr):
    sum = 0
    for i in arr:
         sum = sum + i
    print (sum)
    return (sum)
    arr1  =  [2, 3, 5]
    res = sumofArray (arr1)
    print (res)


class PrimeTest (unittest.TestCase):
    def testcase1 (self):
        self.assertEqual (sumofArray ([2, 3, 5]), 10)

    def testcase2 (self):
        self.assertEqual (sumofArray ([2, 3, 5, 5, 5]), 11)
