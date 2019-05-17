f = open('rosalind_tree.txt')

list = []
for line in f:
    list.append(line)

list = list[1:]

# print (list)
new_list = []
for item in list:
    new_list.append(item.strip('\n'))

# print (new_list)

string = ''
for i in range(0,len(new_list[0])):
    string += '0 '

print (string)