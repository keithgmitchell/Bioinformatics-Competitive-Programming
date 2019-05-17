from Bio import SeqIO
from Bio.SeqUtils import GC

records = list(SeqIO.parse("input.txt.txt", "fasta"))

matrix = [[] for i in range(0,len(records))]

def get_mismatches(seq1, seq2):
    count = 0
    for x, y in zip(seq1, seq2):
        if x != y:
            count += 1
    return count/len(seq1)

records2 = records
for record, count in zip(records, range(0,len(records))):
    for record2 in records2:
        matrix[count].append(get_mismatches(record.seq, record2.seq))

for list in matrix:
    print (' '.join([str(i) for i in list]))