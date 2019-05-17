f = open('rosalind_tree.txt')

count = 0
for line in f:
    count += 1
    if not count%2:
        print(line.replace('\n', ''))
