import itertools

number = 5
listA = [i for i in range(0, number+1)]
perm = itertools.permutations(listA)
perm_count = itertools.permutations(listA)

print(len([k for k in perm_count]))
for i in list(perm):
    print(' '.join([str(j) for j in i]))