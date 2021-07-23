import unittest


import unittest


def sumofpair (arr, sum):
    arr.sort ()#sort the array
    left = 0
    print(arr)
    right = len (arr) - 1
    res = []
    while left <= right:
        if arr [left] + arr [right] > sum:
            right = right - 1
        elif arr [left] + arr [right] < sum:
            left = left + 1
        elif arr [left] + arr [right] == sum:
            print ("Values of pair are", arr [left], "&", arr [right])
            res.append (arr [left])
            res.append (arr [right])
            right = right - 1
            left = left + 1
    return res
arr = [3, 4, 56, 11, 10, 9, 5]
sum = 15
sumofpair (arr,sum)

class sumofpair_test (unittest.TestCase):

    def testcase2 (self):
        arr = [3, 4, 56, 11, 10, 9, 5]
        sum = 15
        expected = [4,11,5,10 ]
        self.assertEqual (expected, sumofpair (arr,sum))






