from Bio import SeqIO

records = SeqIO.parse('rosalind_tree.txt','fasta')
records_list = []
for i in records:
    records_list.append(i.seq)

main_seq = str(records_list[0])
sub_string = str(records_list[1])

locs = []
mindex = 0
for sbase in sub_string:
    base_not_found = True
    while base_not_found:
        if sbase == main_seq[mindex]:
            locs.append(mindex+1)
            base_not_found = False
        mindex += 1

print(' '.join([str(i) for i in locs]))