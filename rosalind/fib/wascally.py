f = open('rosalind_tree.txt')

list = []
for line in f:
    list.append(line)
list[0] = list[0].split(' ')
months, repro = int(list[0][0]), int(list[0][1])

def fibo(months, repro):
    if months <= 1:
        return 1

    elif months == 2:
        return repro

    if months <= 4:
        return fibo(months-1, repro) + fibo(months-2, repro)

    return fibo(months - 1, repro) + fibo(months-2, repro) * repro


print(fibo(months, repro))
