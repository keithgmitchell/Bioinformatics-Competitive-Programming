from Bio import SeqIO

records = SeqIO.parse('rosalind_tree.txt','fasta')
records_list = []
for i in records:
    records_list.append(i.seq)

seq_1 = str(records_list[0])
seq_2 = str(records_list[1])

transitions = 0
transversions = 0
for x,y in zip(seq_1, seq_2):
    if x == 'C' and y == 'T':
        transitions += 1
    elif x == 'T' and y == 'C':
        transitions += 1
    elif x == 'A' and y == 'G':
        transitions += 1
    elif x == 'G' and y == 'A':
        transitions += 1
    elif x == y:
        pass
    else:
        transversions += 1

print(transitions/transversions)

