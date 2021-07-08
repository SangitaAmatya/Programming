def missingno(A):
    n = len(A)
    total = (n+1)*(n+2)/2
    sumofA= sum(A)
    return total - sumofA
A = [ 1, 2,3,5,6 ]
miss =  missingno(A)
print(miss)
