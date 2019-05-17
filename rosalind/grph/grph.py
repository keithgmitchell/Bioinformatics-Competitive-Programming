from Bio import SeqIO
from Bio.SeqUtils import GC

def find_addjacent(records, item):
    for record in records:
        if record.seq[0:3] == item.seq[len(item.seq)-3::] and record.description != item.description:
            print(item.description + ' ' + record.description)

records = list(SeqIO.parse("rosalind_tree.txt", "fasta"))

for item in records:
    find_addjacent(records, item)


