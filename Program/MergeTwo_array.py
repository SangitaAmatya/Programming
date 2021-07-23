A = [2, 4, 6, 8]
B = [1, 3, 5, 7, 9]

print ("Array of A : ",A)
print ("Array of B : ",B)
def merge (list1, list2, m, n):  # Function definition
    i = 0
    j = 0
    c = []  # empty list c which is also the merged list
    while (i < m and j < n):
        if list1 [i] <= list2 [j]:
            c.append (list1 [i])
            i += 1
        else:
            c.append (list2 [j])
            j += 1
    for p in range (i, m):  # To put the remaining elements into c
        c.append (list1 [p])
    for q in range (j, n):
        c.append (list2 [q])
    print ("After merging the array",c)
    c.reverse()
    print(c)
merge (A, B, len (A), len (B)) # Function call