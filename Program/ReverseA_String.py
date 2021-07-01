#In above code, we call a function to reverse a string,
#which iterates to every element and intelligently join each character
#in the beginning so as to obtain the reversed string.
#s=input("enter string : ")
#print(s[::-1])

# Python code to reverse a string
# using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def RevesrseA_String(string):
    str1 = reverse(string)
    print("String in reverse Order :  ", str1)

    if (string == str1):
        return True
    else:
        return False
