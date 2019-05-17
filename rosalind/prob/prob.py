import math


def get_prob(seq, prob):
    p = 1
    for base in seq[0]:
        if base == 'A' or base == 'T':
            p *= (1-float(prob))/2
        else:
            p *= (float(prob))/2
    return p

file = []
f = open('rosalind_tree.txt')

# get file contents
for line in f:
    line = line.replace('\n', '')
    file.append(line.split(' '))

# print list of results
list = []
for prob in file[1]:
    list.append((math.log10(get_prob(file[0], prob))))

print(' '.join([str(item) for item in list]))