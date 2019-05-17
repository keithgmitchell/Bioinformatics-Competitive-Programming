f = open('input.txt')

file = []
for line in f:
    line = line.replace('\n', '')
    line = line.split(' ')
    line = [int(i) for i in line]
    file.append(line)

sols = []
for line in file[1:]:
    found = False
    for item in line:
        if item < 0 and abs(item) <= file[0][1] and abs(item) in line:
            found = True
            if line.index(item) < line.index(abs(item)):
                sols.append([line.index(item)+1, line.index(abs(item))+1])
            elif line.index(abs(item)) < line.index(item):
                sols.append([line.index(abs(item))+1, line.index(item)+1])

        if found == True:
            break
    if found == False:
        sols.append([-1])

print(sols)

for item in sols:
    print(' '.join([str(x) for x in item]))

