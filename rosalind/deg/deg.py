f = open('input.txt')

file = []
for line in f:
    line = line.replace('\n', '')
    file.append(line.split(' '))

for item in file:
    print(item)

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
for i in range(1, len(dict.keys())+1):
    lens.append(len(dict[str(i)]))

print(' '.join([str(x) for x in lens]))
