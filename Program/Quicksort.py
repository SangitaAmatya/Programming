import unittest


def quicksort(list1):
    length = len(list1)
    if length<=1:
        return list1
    else :
        pivot = list1.pop()
        item_grater = []
        item_lower  = []
        for item in list1:
            if item > pivot:
                item_grater.append(item)
            else:
                item_lower.append((item))

    return quicksort (item_lower)+[pivot]+quicksort((item_grater))
print(quicksort(([4,33,7,9,2])))
class IsSortedTest(unittest.TestCase):
    def test_merge_sort_on_sorted_integers(self):
        list1 = [4,33,7,9,2]
        self.assertEqual([2, 4, 7, 9, 33],quicksort ( list1))

    def test_merge_sort_on_sorted_integers1 (self):
        list1=[1,4,6,3]
        self.assertEqual([1,3,4,6],quicksort ( list1))


