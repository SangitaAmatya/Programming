import unittest


def sumofpair (arr, sum):
    arr.sort ()#sort the array
    left = 0
    right = len (arr) - 1
    while left <= right:
        if arr [left] + arr [right] > sum:
            right = right - 1
        elif arr [left] + arr [right] < sum:
            left = left + 1
        elif arr [left] + arr [right] == sum:

            print ("Values of pair are", arr [left], "&", arr [right])
            right = right - 1
            left = left + 1

arr = [3, 4, 56, 11, 10, 9,5]
sum = 15
sumofpair (arr, sum)
##anotherway



# Returns number of pairs
# in arr[0..n-1] with sum
# equal to 'sum'
def printPairs (arr, n, sum):
    # count = 0

    # Consider all possible
    # pairs and check their sums
    for i in range (0, n):
        for j in range (i + 1, n):
            if (arr [i] + arr [j] == sum):
                print ( arr [i],"&", arr [j])
# Driver Code
arr = [1, 5, 7, -1, 5]
n = len (arr)
sum = 6
printPairs (arr, n, sum)
