
import itertools
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

number = 956
listA = [i for i in range(1, number+1)]
total_sum = 0
for i in range(1, number+1):
    # perm = itertools.combinations(listA, i)
    # perm_count = itertools.combinations(listA, i)
    # # print(len([k for k in perm_count]))
    # # print(list(perm))
    # master_list.append(list(perm))
    # total_sum += len([k for k in perm_count])
    total_sum += ncr(number, i)
    print(i, total_sum)

print ((total_sum+1) % 1000000)