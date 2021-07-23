import unittest


def checktheparenthsis (parentheses):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    map = dict (zip (open_list, close_list))#zip 2 lists into a nested dict
    a = []
    for i in parentheses:
        if i in open_list:
            a.append (map [i])
        elif i in close_list:
            if not a or i != a.pop ():
                return "unbalance"
            if not a:
                return "balance"
            else:
                "unbalance"


string = "{[]{()}}"
print (string, "-", checktheparenthsis (string))

string = "((()"
print (string, "-", checktheparenthsis (string))
class Test(unittest.TestCase):

    def test_1(self):
       expected = "balance"
       self.assertEqual(expected,checktheparenthsis("{[]{()}}"),True)

    def test_2 (self):
           expected = "unbalance"
           self.assertEqual (expected, checktheparenthsis ("{[{()))))))}}"))
