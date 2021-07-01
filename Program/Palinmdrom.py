
import unittest
def reverse(str1):
    if (len(str1) == 0):
        return str1
    else:
        return reverse(str1[1:]) + str1[0]

def checkPalindrom(string):
    str1 = reverse(string)
    print("String in reverse Order :  ", str1)

    if (string == str1):
        return True
    else:
        return False

