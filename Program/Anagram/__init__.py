
# anagram or not
import unittest


def checkAnagram (s1, s2):
    # the sorted strings are checked
    if (sorted (s1) == sorted (s2)):
        return ("The strings are anagrams.")
    else:
       return ("The strings aren't anagrams.")

    # driver code


s1 = "raj"
s2 = "jar"
checkAnagram (s1, s2)
class checkAnagram (unittest.TestCase):

    def test_bubble_sort_with_positive_numbers (self):
        s1 = "raj"
        s2 = "jar"
        print(self.assertEqual ("The strings are anagrams.",checkAnagram (s1, s2)))
