import unittest


def Intersection (arr1, arr2, m, n):
    i, j = 0, 0
    res = []
    while i < m and j < n:
        if arr1 [i] < arr2 [j]:
            i += 1
        elif arr2 [j] < arr1 [i]:
            j += 1
        else:
            print (arr2 [j])
            j += 1
            i += 1


# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len (arr1)
n = len (arr2)
Intersection (arr1, arr2, m, n)

#another way
def intersection (lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
# Driver Code
lst1 = [1,2,4,5]
lst2 = [1,3,4,5]
print (intersection (lst1, lst2))
class intersection (unittest.TestCase):
    def testcase2 (self):
            self.assertEqual(intersection ([1, 2, 3, 4], [2, 3]) == [2, 3])

    def test_mergesort_negative_numbers_only (self):
     self.assertEqual ([-9, -7, -5, -5, -3, -1],intersection  ([5, 5, 7, 8, 2, 4, 1]), True)


