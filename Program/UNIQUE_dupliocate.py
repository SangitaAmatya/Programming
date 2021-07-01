import unittest
def UNIQUE_dupliocate  (list_value):
    #inset the list to the set
    list_set = set(list_value)
    #convert the set to the list
    unique_list = list(list_set)
    for x in unique_list :
     print(x)

    list1 = unique_list(list_value)
    print("\nThe unique values of List")
    UNIQUE_dupliocate (list1)

    class PalindromeTest(unittest.TestCase):
        def testcase1(self):
            self.assertEqual(UNIQUE_dupliocate[2, 2, 3, 1, 4, 2])
    #[1,1,2,4,3,4]
    #[sangita,sangita,a,b,b]