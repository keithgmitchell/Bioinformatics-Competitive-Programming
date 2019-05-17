from Bio import SeqIO
import urllib
import requests

def check_position(index, sequence, places_found):
    if sequence[index+1] != 'P' and (sequence[index+2] == 'S' or sequence[index+2] == 'T') and sequence[index+3]!= 'P':
        places_found.append(index+1)
        return places_found


proteins = []
input = open('mprt.txt')
for line in input:
    proteins.append(line.replace('\n', ''))

print (proteins)
for protein in proteins:
    url = 'https://www.uniprot.org/uniprot/%s.fasta' % (protein)
    fasta = requests.get(url).text
    sequence = ''.join(fasta.split('\n')[1:])
    places_found = []
    index = 0
    for base in sequence:
        if base == 'N':
            check_position(index, sequence, places_found)
        index += 1
    if len(places_found):
        print(protein)
        print(' '.join([str(i) for i in places_found]))
