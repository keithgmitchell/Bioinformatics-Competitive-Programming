n = 21

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)


def fib_effecient(n):
    if n == 0:
        return 0
    array = [0 for i in range(0,n+1)]
    array[0] = 0
    array[1] = 1
    for i in range(2,n+1):
        array[i] = array[i-1] + array[i-2]
    return array[n]

print(fib1(n))
print(fib_effecient(n))