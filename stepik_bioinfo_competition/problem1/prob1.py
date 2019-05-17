import numpy
import sys

sys.setrecursionlimit(11000)

f = open('rosalind_tree.txt')

my_list = []

i = 0
for line in f:
    line = line.split(' ')
    if i == 0:
        n, m, k = line[0], line[1], line[2]
        print (n,m,k)
    else:
        my_list.append([line[0], line[1], line[2].strip('\n'), i])
    i += 1
    
traversal = []
matrix = []
for i in my_list:
    matrix.append(list(map(int, i)))
cur_traversal = []
print (matrix)

path = []
vertex = 5
def recursive_traverse(matrix, vertex, past_index, path, length):
    
    for row, index in zip(matrix, range(0, len(matrix))):
        
        if len(path) == length:
            return path
        elif index == past_index:
            continue
        elif row[2] == 0:
            matrix[index] = [0, 0, 0, 0]
        elif row[0] == vertex:
            matrix[index] = row[0], row[1], row[2]-1, row[3]
            recursive_traverse(matrix, row[1], index, path + [row[3]], length)
        elif row[1] == vertex:
            matrix[index] = row[0], row[1], row[2]-1, row[3]
            recursive_traverse(matrix, row[0], index, path + [row[3]], length)
        

def split_matrix(matrix):
    matrix_list = []
    value_list = []
    index_l = []
    for i in range(0,5):
        for row, index in zip(matrix, range(0, len(matrix))):
            # print (row)
            if len(value_list)==0:
                value_list.append([row[0], row[1]])
                index_l.append(index)
                continue
            for list in value_list:
                if row[0] in list or row[1] in list:
                    list += [row[0], row[1]]
                    if index not in index_l:
                        index_l.append(index)

    return value_list, index_l, matrix


print(recursive_traverse(matrix, 2, -1, path, 7))


# for i in range(0,1000):
#     matrix_list = []
#     result = (split_matrix(matrix))
#     # print (result)
#     new_matrix = [matrix[i] for i in result[1]]
#     print (new_matrix)
#     print (sum(row[2] for row in new_matrix))
#     print (recursive_traverse(new_matrix, 2, -1, path, sum(row[2] for row in new_matrix)))
#     matrix = [x for x in matrix if x not in new_matrix]
#     if len(matrix) == 0:
#         break





