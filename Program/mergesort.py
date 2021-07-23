import unittest

def mergeSort(arr):

    if len(arr)>1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
#recussion
        mergeSort(left_arr)
        mergeSort(right_arr)
        i=j=k=0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i=i+1
            else:
                arr[k]=right_arr[j]
                j=j+1
            k=k+1

        while i < len(left_arr):
            arr[k]=left_arr[i]
            i=i+1
            k=k+1

        while j < len(right_arr):
            arr[k]=right_arr[j]
            j=j+1
            k=k+1
    return arr
arr_tset = [1,4,3,2,7,6,8,10,9]
mergeSort(arr_tset)
print(arr_tset)
class IsSortedTest(unittest.TestCase):
    def test_merge_sort_on_sorted_integers(self):
     self.assertEqual ([1, 2, 4, 5,5, 7, 8], mergeSort ([5, 5, 7, 8, 2, 4, 1]), False)
    def test_mergesort_negative_numbers_only (self):

     self.assertEqual ([-9, -7, -5, -5, -3, -1], mergeSort ([5, 5, 7, 8, 2, 4, 1]), True)


