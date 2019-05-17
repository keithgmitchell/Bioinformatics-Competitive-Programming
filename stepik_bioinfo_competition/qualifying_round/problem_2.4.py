import csv
import os
from Bio import pairwise2


def transform(string):
    master_string = ''
    count = 1
    for i in range(0, len(string)):
        if i == 0:
            continue
        elif string[i] == string[i-1]:
            count += 1
        else:
            master_string += str(count) + string[i-1]
            count = 1
    master_string += str(count) + string[i]
    return master_string




def solve_problem(number, length, edit_distance, string):

    # first lets iterate through each segment of the sequence with length as specified for the problem.
    for i in range(0, len(string)-length):
        # print (i)
        query = string[i:i+length]
        # query = query[::-1]
        count = 0
        x_list = []
        jump=False
        x = length
        # the query string, or segment, should be compared to all other combinations in the string.
        while x < len(string)-length:
            if x in range(i,i+length):
                x+=1
                continue
            if jump == True:
                x = x + length
                # print (x)

            compare = string[x:x+length]

            align = pairwise2.align.globalxx(compare, query)
            # M X I D
            type = ''
            seqcount = 0
            errors = 0
            type_list = ''
            for m,n in zip(align[0][0], align[0][1]):
                if m==n:
                    if type!='M':
                        type = 'M'
                        seqcount = 0
                    seqcount += 1

                elif m=='-':
                    if type!='I':
                        type = 'I'
                        seqcount = 0
                    seqcount += 1
                    errors += 1

                elif n=='-':
                    if type!='D':
                        type = 'D'
                        seqcount = 0
                    seqcount += 1
                    errors += 1

                else:
                    if type!='X':
                        type = 'X'
                        seqcount = 0
                    seqcount += 1
                    errors += 1
                type_list += type

            if errors <= edit_distance:
                count += 1
                x_list.append([x+1, transform(type_list), align])
                # print(x)
                print(compare, query, x+1, type_list, len(type_list))
                jump=True
                x+=1
            else:
                jump=False
                x+=1

        # if we find the number we are look for based on a condition then we will output and return 0
        if count >= number:
            print (query)
            for i in x_list:
                print (i[0], i[1])
                # print (pairwise2.format_alignment(*i[2][0]))
            return 0

# read in a file
with open('tests/3.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    list = []
    for row in reader:
        list.append(row)

# list[0] = number, length, edit_distance
# list[1] = sequence,

solve_problem(int(list[0][0]), int(list[0][1]), int(list[0][2]), list[1][0])
# solve_problem(2,7,3, 'GAGTCATCGGACGATCC')
# align = pairwise2.align.globalxx("ACGATCC", "ACGTAGC")
# print (align[0])
