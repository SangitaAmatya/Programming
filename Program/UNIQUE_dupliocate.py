# Python program to check if two
# to get unique values from list
# using set

# function to get unique values
import unittest
from collections import Counter


def unique (list1):

    print ("the unique values from 1st list is")


    # insert the list to the set
    list_set = set (list1)
    # convert the set to the list
    unique_list = (list (list_set))
    for x in unique_list:
        #return (list_set)
        print(x)

list1l = [1,2,2,4,5,6,7,6,8]

my_list = sorted (list1l)

duplicates = []
for i in my_list:
    if my_list.count (i) > 1:
        if i not in duplicates:
            duplicates.append (i)

            print(duplicates)

print ("the duplicate values from 1st list is")
unique (list1l)
class TestBubbleSortVOneAlgorithm(unittest.TestCase):

    def test_bubble_sort_with_positive_numbers(self):
        list1l = [1, 2, 2, 4, 5, 6, 7, 6, 8]
        self.assertEqual([1,2,4,5,6,7,8],unique( list1l))



