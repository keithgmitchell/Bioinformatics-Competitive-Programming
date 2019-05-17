f = open('input.txt')

file = []
for line in f:
    line = line.replace('\n', '')
    file.append(line.split(' '))

dict = {}
for i in range(1,len(file)):
    if file[i][0] in dict.keys():
        dict[file[i][0]].append(file[i][1])
    else:
        dict[file[i][0]] = [file[i][1],]

    if file[i][1] in dict.keys():
        dict[file[i][1]].append(file[i][0])
    else:
        dict[file[i][1]] = [file[i][0],]

lens = []
for i in range(1, int(file[0][0])+1):
    sum = 0
    if str(i) in dict.keys():
        for y in dict[str(i)]:
            sum += len(dict[str(y)])
    lens.append(sum)
print(' '.join([str(x) for x in lens]))
