f = open('input.txt')

file = []
for line in f:
    line = line.replace('\n','')
    file.append([int(x) for x in line.split(' ')])

components = []
pos = 0
for object in file[1:]:
    if pos == 0:
        components.append(object)
    else:
        found = False
        for component in components:
            if object[0] in component and object[1] in component:
                found = True
                break
            elif object[0] in component or object[1] in component:
                found = True
                component += [object[0], object[1]]
                break
        if found == False:
            components.append(object)
    pos += 1

for x in range(1,file[0][0]+1):
    found = False
    for item in components:
        if x in item:
            found = True
    if found == False:
        components.append([x])


print (len(components))

for item in components:
    print (item)