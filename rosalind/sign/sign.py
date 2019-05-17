import itertools

number = 6
listA = [i for i in range(number, -1*(number+1), -1)]
listA.remove(0)
perm = itertools.permutations(listA, 2)
perm_count = itertools.permutations(listA, 2)

count = 0
for item in list(perm):
    if abs(item[0]) != abs(item[1]):
        count += 1
        print(' '.join([str(j) for j in item]))
print(count)