n = 85
k = 9


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def permutation(n,k):
    return (factorial(n))/(factorial(n-k))

print(permutation(n,k)%1000000)