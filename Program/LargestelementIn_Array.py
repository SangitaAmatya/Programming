import unittest


# in arr[] of size n
# python function to find maximum
# in arr[] of size n
def largest (arr, n):
    # Initialize maximum element
    max = arr [0]
    # Traverse array elements from second
    # and compare every element with 
    # current max
    for i in range (1, n):
        if arr [i] > max:
            max = arr [i]
            return max

# Driver Code
# arr = [10, 324, 45, 90, 9808]
# n = len (arr)
# ans = largest (arr, n)
# print ("Largest in given array is", Ans)
class LargestArrayInaArrayTest (unittest.TestCase):
    def testcase1 (self):
        self.assertEqual (largest ([10, 324, 45, 90, 9808]), 9808)
