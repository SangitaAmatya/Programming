import unittest


def test_for_anagrams (s1, s2):
    # the sorted strings are checked
    if (sorted (s1) == sorted (s2)):
        return "The strings are anagrams."
    else:
        return "The strings aren't anagrams."

    # driver code

    s1= "raj"
    s2 = "jar"
# Main Program
#s1 = input ("Enter a string 1: ")
#s2 = input ("Enter a string 2: ")
    result = test_for_anagrams (s1, s2)
    print (result)
class checkAnagram (unittest.TestCase):

    def test_test_for_anagrams1 (self):
        s1 = "mhmh"
        s2 = "mmhh"

        self.assertEqual ("The strings are   anagrams.",test_for_anagrams (s1, s2))

    def test_test_for_anagrams2 (self):
            s1 = "sssss"
            s2 = "mmhh"

            self.assertEqual ("The strings aren't anagrams..", test_for_anagrams (s1, s2))