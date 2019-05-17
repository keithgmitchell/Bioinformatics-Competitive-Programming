f = open('input.txt')
list = []
for line in f:
    list.append(line)

from Bio.Seq import Seq
my_seq = Seq(list[0])
print(my_seq.count("A"), my_seq.count('C'), my_seq.count('G'), my_seq.count('T'))