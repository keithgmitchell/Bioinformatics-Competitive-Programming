f = open('rosalind_tree.txt')

file = []
for line in f:
    line = line.replace('\n', '')
    file.append(line.split(' '))


k_gen = file[0][0]
N = file[0][1]





