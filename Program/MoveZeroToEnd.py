# Python3 code to move all zeroes
# at the end of array

# Function which pushes all
# zeros to end of an array.
import unittest
def pushZerosToEnd (arr):
    n = len (arr)
    count = 0  # Count of non-zero elements
    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range (n):
        if arr [i] != 0:
            # here count is incremented
            arr [count] = arr [i]
            count += 1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr [count] = 0
        count += 1
        #unit testcase
    #return arr

# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
pushZerosToEnd (arr)
print ("Array after pushing all zeros to end of array:")
print (arr)
class pushZerosToEndTest (unittest.TestCase):
    def testcase1 (self):
        expected = [0, 0, 1, 2, 3]
        self.assertEqual (expected, pushZerosToEnd ([1, 0, 2, 3, 0]))
