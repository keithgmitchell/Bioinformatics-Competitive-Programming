f = open('rosalind_tree.txt')

list= []
for line in f:
    list.append(line)

list[1]= list[1].split(' ')
print (str(list[0][int(list[1][0]):int(list[1][1])+1]) + ' ' + str(list[0][int(list[1][2]):int(list[1][3])+1]))