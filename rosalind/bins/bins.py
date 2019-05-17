f = open('input.txt')

file = []
for line in f:
    line = line.replace('\n', '')
    file.append(line.split(' '))

list1 = file[2]
list2 = file[3]

pos = []
for item in list2:
    if item in list1:
        pos.append(list1.index(item)+1)
    else:
        pos.append(-1)

print(' '.join([str(x) for x in pos]))

