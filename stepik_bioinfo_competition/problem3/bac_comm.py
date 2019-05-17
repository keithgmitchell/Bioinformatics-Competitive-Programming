from collections import Counter
import operator
import numpy

def dict_simlarity_score(dict1, dict2):
    score = 0
    # if len(dict1.keys() & dict2.keys()):
        # print ("TRUE")
    for n,m in zip(dict1.keys(), dict2.keys()):
        if n in dict2.keys():
            score += (dict2[n]+dict1[n])
        if m in dict1.keys():
            score += (dict2[m]+dict1[m])

    for first in dict1.keys():
        for second in dict2.keys():
            if first != second:
                count = sum(1 for a, b in zip(first, second) if a != b)
                if count <= 1:
                    score += dict1[first] + dict2[second]
                elif count == 2:
                    score += (dict1[first] + dict2[second])/2
    return score


f = open('rosalind_tree.txt')

generation_list = []
allsets = []
for line in f:
    # print (line)
    if len(line.split(' ')) == 1:
        # print('number')
        allsets.append(generation_list)
        generation_list = []
    else:
        generation_list.append(line.strip('\n').split(' '))

allsets.append(generation_list)
allsets = allsets[2:]

master_list = []
new_answer_list = []

for community in allsets:
    # matrix = [[0 for x in range(0,len(community))] for i in range(0,len(community))]
    # print (matrix)
    print('')
    print('######## NEW SET ###########')

    generation_num = 0
    answer_list = []
    dict_list = []
    for generation in community:

        a = dict(Counter(generation))
        dict_list.append(a)
        a = sorted(a.items(), key=operator.itemgetter(1))
        answer_list.append([generation_num, len(a)])
        generation_num += 1

    # print (answer_list)
    list_sort = sorted(answer_list, key=lambda tup: tup[1])
    list_sort = [i[0] for i in list_sort]
    # print (dict_list)
    master_list.append(list_sort)

    matrix = [[0 for x in range(0, len(dict_list))] for i in range(0, len(dict_list))]
    for x in range(0, len(dict_list)):
        for y in range(0, len(dict_list)):
            if x != y:
                matrix[x][y] = dict_simlarity_score(dict_list[x], dict_list[y])
    matrix = numpy.array(matrix)
    index = list_sort[0]
    new_temp_answer_list = []
    h = 0
    add_another = True
    while h < len(community)-1:
        result = numpy.where(matrix[index] == numpy.amax(matrix[index]))
        print (numpy.amax(matrix[index]))

        if numpy.amax(matrix[index]) == 0:
            print ("BREAK")
            missing_values = (list(set(list_sort) - set(new_temp_answer_list)))
            missing_values = [ele for ele in list_sort if ele not in new_temp_answer_list]
            print (missing_values)
            new_temp_answer_list += missing_values
            h = len(community)
            add_another = False

        print (result[0][0], index)
        result = result[0][0]
        matrix[:, index] = 0
        matrix[index] = 0
        if add_another:
            new_temp_answer_list.append(index)
        index = result
        h+=1
    if add_another:
        new_temp_answer_list.append(index)
    new_answer_list.append(new_temp_answer_list)

print ('')

for object in master_list:
    print (' '.join(str(e) for e in object))

print ('')

for object in new_answer_list:
    print (' '.join(str(e) for e in object))