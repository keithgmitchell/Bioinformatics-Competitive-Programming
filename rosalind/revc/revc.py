f = open('rosalind_revc (1).txt')
for i in f:
    string = i

new_string = ''
for i in string:
    if i == 'A':
        new_string += 'T'
    if i == 'T':
        new_string += 'A'
    if i == 'C':
        new_string += 'G'
    if i == 'G':
        new_string += 'C'


print (new_string[::-1])