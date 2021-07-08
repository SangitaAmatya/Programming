def Reverse (lst):
    lst.reverse ()
    return lst

lst = [10, 11, 12, 13, 14, 15]
print (Reverse (lst))
#2.Using the slicing technique.
def Reverse (lst):
    new_lst = lst [::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print (Reverse (lst))