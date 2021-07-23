import unittest
#1. User must enter a string.
#2. The string is passed as
#an argument to a recursive function.
#3. In the function, if the length of the string is less than 1, True is returned.
#4. If the last letter is equal to the first letter, the function is called recursively
# with the argument as the sliced list with the first character
# and last character removed, else return False.
# The if statement is used to check if the returned value is True or False and the final result
# is printed.

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a="mama"
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")


class PalindromeTest (unittest.TestCase):
    def testcase1 (self):
        self.assertEqual (is_palindrome ("tat"), False)

    def testcase2 (self):
            self.assertEqual (is_palindrome ("tata"), True)
