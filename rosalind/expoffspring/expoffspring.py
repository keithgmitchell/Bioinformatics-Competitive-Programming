f = open('rosalind_tree.txt')

list = []

for line in f:
    list.append(line)
list[0] = list[0].split(' ')

frac = [1, 1, 1, 0.75, 0.5, 0]

sum = 0
for x, y in zip(list[0], frac):
    sum+= (int(x)*y)*2

print (sum)