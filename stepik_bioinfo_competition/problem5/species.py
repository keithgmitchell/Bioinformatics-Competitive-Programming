import operator
import numpy

f = open('rosalind_tree.txt')

def quantify(list1, list2):
    count = 0
    # the first list is the male, the second list is the female.
    for n, m in zip(list1, list2):
        # Homozygous situatious
        if n[0] == '1' and n[1] == '1' and m[0] == '1' and m[1] == '1':
            count += 0
        if n[0] == '1' and n[1] == '1' and m[0] == '0' and m[1] == '0':
            count += 1
        if n[0] == '0' and n[1] == '0' and m[0] == '1' and m[1] == '1':
            count += 1
        if n[0] == '0' and n[1] == '0' and m[0] == '0' and m[1] == '0':
            count += 0
        else:
            count += 0.5

        # # Heterozygous situations
        # if n[0] == '1' and n[1] == '0' and m[0] == '0' and m[1] == '0':
        #     count += 0.5
        # if n[0] == '0' and n[1] == '1' and m[0] == '0' and m[1] == '0':
        #     count += 0.5
        # if n[0] == '0' and n[1] == '0' and m[0] == '1' and m[1] == '0':
        #     count += 0.5
        # if n[0] == '0' and n[1] == '0' and m[0] == '0' and m[1] == '1':
        #     count += 0.5
        #
        # # Heterozygous situations
        # if n[0] == '1' and n[1] == '0' and m[0] == '1' and m[1] == '0':
        #     count += 0.5
        # if n[0] == '0' and n[1] == '1' and m[0] == '0' and m[1] == '1':
        #     count += 0.5
        # if n[0] == '0' and n[1] == '0' and m[0] == '1' and m[1] == '0':
        #     count += 0.5
        # if n[0] == '0' and n[1] == '0' and m[0] == '0' and m[1] == '1':
        #     count += 0.5
        #

    return count


# def update_matrix(col, matrix):
#     for row in matrix:
#         print (row)
#         ma


list = []
for line in f:
    list.append(line)

new_list = []
temp_list = []
for object in list:
    temp_object = object.strip('\n').split('/')
    if len(temp_object)>1:
        temp_list.append(temp_object)
    else:
        new_list.append(temp_list)
        temp_list = []
new_list.append(temp_list)

print (len(new_list)/2, new_list)

n = len(new_list)/2
matrix = [[0 for x in range(0, int(n))] for i in range(0, int(n))]

male_list = new_list[0:int(n)]
female_list = new_list[int(n):]

for x in range(0,int(n)):
    for y in range(0, int(n)):
        matrix[x][y] = quantify(male_list[x], female_list[y])

for row in matrix:
    print (row)

matrix = numpy.array(matrix)
answer_list = [0 for i in range(0,int(n))]




for male_index in range(0,int(n)):
    # index, value = max(enumerate(matrix[male_index]), key=operator.itemgetter(1))
    result = numpy.where(matrix == numpy.amax(matrix))
    listOfCordinates = (zip(result[0], result[1]))
    cord_list = [cord for cord in listOfCordinates]
    print(cord_list)
    answer_list[cord_list[0][0]] = cord_list[0][1] + 1
    matrix[:, cord_list[0][1]] = 0
    matrix[cord_list[0][0]] = 0

    print (matrix)
    print (answer_list)

for item in answer_list:
    print (item)
