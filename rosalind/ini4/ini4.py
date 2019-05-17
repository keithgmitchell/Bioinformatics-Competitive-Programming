int1 = 4083
int2 = 8141
sum = 0
for i in range(int1, int2+1):
    if i % 2:
        sum += i
print(sum)