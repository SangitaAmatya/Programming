import unittest


def mergeSort (myList):
    if len (myList) > 1:
        mid = len (myList) // 2
        left = myList [:mid]
        right = myList [mid:]

        # Recursive call on each half
        mergeSort (left)
        mergeSort (right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len (left) and j < len (right):
            if left [i] <= right [j]:
                # The value from the left half has been used
                myList [k] = left [i]
                # Move the iterator forward
                i += 1
            else:
                myList [k] = right [j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len (left):
            myList [k] = left [i]
            i += 1
            k += 1

        while j < len (right):
            myList [k] = right [j]
            j += 1
            k += 1
    return myList;

myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
reslist = mergeSort (myList)
print (reslist)


class IsSortedTest(unittest.TestCase):
    def test_merge_sort_on_sorted_integers(self):
        myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.assertEqual([17, 20, 26, 31, 44, 54, 55, 77, 93],mergeSort (myList))
        myList = [54, 0, 93, 17, 17, 5, 44, 55, 0]
        self.assertEqual([0, 0, 5, 17, 17, 54, 55, 77, 93],mergeSort (myList))


