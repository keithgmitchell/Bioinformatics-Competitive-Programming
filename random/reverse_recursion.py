list = [1,2,3,4,5,6,7,8,9,0]

def reverse(list, new_list):
    if len(list) == 0:
        print (new_list)
        return [i for i in new_list]
    new_list.append(list[len(list)-1])
    del list[len(list)-1]
    reverse(list, new_list)

