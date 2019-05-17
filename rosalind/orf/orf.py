f = open('input.txt.txt')

table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop',
        'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W',
    }

# returns the reverse complement
master_proteins = []
def complements(seq):
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    string = ''
    for i in seq:
        string += complements[i]
    return string[::-1]

# prints remaining protein given a start position
def orf_print(seq, pos):
    prot = []
    i = pos
    while i < len(seq)-3:
        if table[seq[i:i + 3]] == 'Stop':
            master_proteins.append(prot)
            return 0
        else:
            prot.append(table[seq[i:i + 3]])
            i += 3


# take the file in
list = []
for line in f:
    list.append(line.strip('\n'))

dna = list[1]
complement = complements(dna)

# find orf in original dna sequence
for pos in range(0,len(dna)-3):
    if table[dna[pos:pos+3]] == 'M':
        orf_print(dna, pos)

# find orf in the reverse complement
for pos in range(0,len(complement)-3):
    if table[complement[pos:pos+3]] == 'M':
        orf_print(complement, pos)

# remove any duplicates
filtered_proteins = []
for i in master_proteins:
    if i not in filtered_proteins:
        filtered_proteins.append(i)

for i in filtered_proteins:
    print(''.join(i))