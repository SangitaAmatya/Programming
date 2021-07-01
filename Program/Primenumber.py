import unittest


def checkPrime(int):
    res = True
    print("Prime number is  :  ", int)
    if int == 1:
        res = False
    if int == 2:
        res = True
    if int > 2:
        for i in range(2, int):
            if (int % i) == 0:
                res = False
                break
            else:
                res = True
    return res


class PrimeTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(checkPrime(1), False)

    def testcase2(self):
        self.assertEqual(checkPrime(2), True)

    def testcase3(self):
        self.assertEqual(checkPrime(3), True)

    def testcase4(self):
        self.assertEqual(checkPrime(4), False)

    def testcase5(self):
        self.assertEqual(checkPrime(15), False)
