f = open('rosalind_tree.txt')

list = []
for line in f:
    line = line.replace('\n', '')
    list.append(line.split(' '))

words = {}
for word in list[0]:
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

for item in words.keys():
    print(item, words[item])