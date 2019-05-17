f = open('rosalind_hamm.txt')

list = []
for i in f:
    list.append(i)

count = 0
for x,y in zip(list[0], list[1]):
    if x == y:
        count += 1

print (len(list[0])-count)