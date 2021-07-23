import unittest
def missingno (A):
    n = len (A)
    total = (n + 1) * (n + 2) / 2
    sumofA = sum (A)
    return total - sumofA
A = [7, 1, 2, 3, 5, 6]
miss = missingno (A)
print (miss)
#Another Way
arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]
missing_elements = []
for ele in range (arr [0], arr [-1] + 1):
    if ele not in arr:
        missing_elements.append (ele)
print (missing_elements)
class Missing_Element(unittest.TestCase):
 def testcase1 (self):
    expected = [8]
    self.assertEqual (expected, missingno ([1, 2, 3, 4, 5, 6, 7, 9, 10]), True)

