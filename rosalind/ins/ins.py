

def insertion_sort(A):
    count = 0
    for i in range(0, len(A)+1):
        k = i
        while k > 0 and k < len(A) and A[k] < A[k-1]:
            count += 1
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1
    return (A, count)

def get_file():
    f = open('input.txt')
    file = []
    for line in f:
        file.append(line)

    n = int(file[0])
    array = [int(x) for x in file[1].split(' ')]
    return(n, array)

n, array = get_file()
print(insertion_sort(array))