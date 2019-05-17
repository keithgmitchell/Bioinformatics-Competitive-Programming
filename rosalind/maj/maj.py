f = open('input.txt')

file = []
for line in f:
    line = line.replace('\n', '')
    file.append(line.split(' '))

sols = []
for line in file[1:]:

    dict = {}
    sum = 0
    for object in line:
        if object in dict.keys():
            dict[object] += 1

        else:
            dict[object] = 1
        sum+=1
    found = False

    for key in dict.keys():
        if dict[key]/sum > 0.5:
            sols.append(key)
            found = True
    if found == False:
        sols.append(-1)


print(' '.join([str(x) for x in sols]))

