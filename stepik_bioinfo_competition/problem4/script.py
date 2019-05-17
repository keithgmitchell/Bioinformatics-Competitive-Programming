f = open('rosalind_tree.txt')

dict = {
        'A': ['GCT', 'GCC', 'GCA', 'GCG'],
        'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'N': ['AAT', 'AAC'],
        'D': ['GAT', 'GAC'],
        'C': ['TGT', 'TGC'],
        'Q': ['CAA', 'CAG'],
        'E': ['GAA', 'GAG'],
        'G': ['GGT', 'GGC', 'GGA', 'GGG'],
        'H': ['CAT', 'CAC'],
        'I': ['ATT', 'ATC', 'ATA'],
        'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'K': ['AAA', 'AAG'],
        'M': ['ATG'],
        'F': ['TTT', 'TTC'],
        'P': ['CCT', 'CCC', 'CCA', 'CCG'],
        'S': ['TCT', 'TCC', 'ACA', 'ACG'],
        'T': ['ACT', 'ACC', 'ACA', 'ACG'],
        'W': ['TGG'],
        'Y': ['TAT', 'TAC'],
        'V': ['GTT', 'GTC', 'GTA', 'GTG'],
        '$': ['TAA', 'TGA', 'TAG']
        }

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
        'TAC':'Y', 'TAT':'Y', 'TAA':'$', 'TAG':'$',
        'TGC':'C', 'TGT':'C', 'TGA':'$', 'TGG':'W',
    }

list = []
for line in f:
    list.append(line.strip('\n'))

dna_string = ''
pos_list = ['' for i in range(0, len(list))]
print (list)
prot_dict = {}
x = 0
for item in list:
    prot_dict[item] = [x, '']
    x+=1
    
list = sorted(list, key=len)
for item in list[::-1]:
    temp_string = ''
    for letter in item:
        temp_string += dict[letter][0]
    if temp_string in dna_string:
        prot_dict[item][1] = ('%s +' % str(dna_string.find(temp_string)+1))
    elif temp_string in dna_string[::-1]:
        print ("REVERSE")
        prot_dict[item][1] = ('%s -' % (len(dna_string) - dna_string[::-1].find(temp_string)+1))
    else:
        prot_dict[item][1] = ('%s +' % str((len(dna_string))+1))
        dna_string += temp_string

print (dna_string)
for item in prot_dict.values():
     pos_list[item[0]] = item[1]

for x in pos_list:
        print(x)