

def merge_sort(A, B):
    master = []
    while len(A) or len(B):
        if len(A) and len(B):
            if A[0] <= B[0]:
                master.append(A[0])
                A.pop(0)
            else:
                master.append(B[0])
                B.pop(0)
        elif len(A):
            master.append(A[0])
            A.pop(0)
        elif len(B):
            master.append(B[0])
            B.pop(0)
    return master

def get_file():
    f = open('input.txt')
    file = []
    for line in f:
        file.append(line)

    A = [int(x) for x in file[1].split(' ')]
    B = [int(x) for x in file[3].split(' ')]
    return A, B

A, B = get_file()
merged = merge_sort(A, B)
print (' '.join([str(i) for i in merged]))