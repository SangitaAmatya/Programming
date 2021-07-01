def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def findevenodd(n):
    if n%2==0:
        return "EVEN"
    else:
        return "ODD"

