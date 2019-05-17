from Bio import SeqIO
from Bio.SeqUtils import GC

records = list(SeqIO.parse("rosalind_tree.txt", "fasta"))

max = 0
max_id = ''
for item in records:
    if (GC(item.seq))> max:
        max = GC(item.seq)
        max_id = item.id

print (max_id)
print (max)