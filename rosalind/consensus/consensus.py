from Bio import SeqIO
import operator

records = list(SeqIO.parse("input.txt", "fasta"))
dict_list = [{} for i in range(0, len(records[0].seq))]

for item in records:
    for letter, index in zip(item.seq, range(0, len(item.seq))):
        if letter in dict_list[index].keys():
            dict_list[index][letter] += 1
        else:
            dict_list[index][letter] = 1
print (dict_list)

cons_string = []
a_list = []
c_list = []
g_list = []
t_list = []
for dictt in dict_list:
    cons_string.append(max(dictt.items(), key=operator.itemgetter(1))[0])
    if 'A' in dictt.keys():
        a_list.append(dictt['A'])
    else:
        a_list.append(0)

    if 'C' in dictt.keys():
        c_list.append(dictt['C'])
    else:
        c_list.append(0)

    if 'G' in dictt.keys():
        g_list.append(dictt['G'])
    else:
        g_list.append(0)

    if 'T' in dictt.keys():
        t_list.append(dictt['T'])
    else:
        t_list.append(0)

print (''.join(cons_string))
print ('A: ', ' '.join([str(x) for x in a_list]))
print ('C: ', ' '.join([str(x) for x in c_list]))
print ('G: ', ' '.join([str(x) for x in g_list]))
print ('T: ', ' '.join([str(x) for x in t_list]))

