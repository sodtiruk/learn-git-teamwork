

def fac1(n):
    if n == 1:
        return 1
    return n * fac1(n-1)

print(fac1(5))