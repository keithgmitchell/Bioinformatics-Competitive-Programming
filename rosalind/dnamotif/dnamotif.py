f = open('rosalind_tree.txt')

list = []

for line in f:
    list.append(line.strip('\n'))

positions = []

print (list)
for index in range(0, len(list[0])-len(list[1])):
    if list[1] == list[0][index:(index+len(list[1]))]:
        positions.append(index+1)

# for index in range(0, len(list[0])-len(list[1])):
#     if list[1] == list[0][::-1][index:(index+len(list[1]))]:
#         positions.append(len(list[0])-index)


print (' '.join([str(i) for i in positions]))