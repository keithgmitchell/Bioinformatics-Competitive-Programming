# f = open('rosalind_tree.txt')
#
# # get list of graph connections
# list = []
# for line in f:
#     line = line.replace('\n', '')
#     line = line.split(' ')
#     if len(line) > 1:
#         list.append(line)
#
# # update the list once by grouping
# # list to be updated and returned as updated list (if applicable)
# # position is the index that we want to check for possible grouping
# def check_if_groups(list, position):
#     index = 0
#     group_found = False
#     for item in list:
#         if index != position:
#             # if tree points in common
#             if set(item) & set(list[position]):
#                 group_found = True
#                 updated_list = list
#                 updated_list[position] = list[index] + list[position]
#                 updated_list.pop(index)
#                 return updated_list, group_found
#         index += 1
#     return list, group_found
#
#
# def recursive_iterations(list, position):
#     result = check_if_groups(list, position)
#     if position == len(list)-1:
#         print(list, len(list))
#         result = check_if_groups(list, position)
#         print(result[0])
#         print(result[1])
#         return None
#     elif result[1] == False:
#         recursive_iterations(list, position+1)
#     else:
#         recursive_iterations(result[0], position)
#
#
# print(recursive_iterations(list, 0))


def problem(n, edges):
    return n - len(edges) - 1

if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open(dirname(__file__) + "/rosalind_tree.txt").readlines()
    n = int(dataset[0])
    edges = []
    for i in range(1, len(dataset)):
        edges.append(list(map(int, dataset[i].split())))
    print(edges, n)
    print (problem(n, edges))