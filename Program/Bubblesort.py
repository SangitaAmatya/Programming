import unittest


def sorting (nums):
    for i in range (len (nums) - 1, 0, -1):
        for j in range (i):
            if nums [j] > nums [j + 1]:
                temp = nums [j]
                nums [j] = nums [j + 1]
                nums [j + 1] = temp
    return nums


nums = [2, 3, 5, 4, 6, 8, 1, 9]
sorting (nums)
print ("After sorting the :", (nums))


class TestBubbleSortVOneAlgorithm (unittest.TestCase):

    def test_bubble_sort_with_positive_numbers (self):
        self.assertEqual ([1, 2, 4, 5, 5, 7, 8], sorting ([5, 5, 7, 8, 2, 4, 1]), True)

    def test_bubble_sort_negative_numbers_only (self):
        self.assertEqual ([-9, -7, -5, -5, -3, -1], sorting ([-1, -3, -5, -7, -9, -5]), False)

    def test_bubble_sort_negative_numbers_only1 (self):
        self.assertEqual ([-9, -7, -5, -5, -3, 0], sorting ([-1, -3, -5, -7, -9, -5]), True)
