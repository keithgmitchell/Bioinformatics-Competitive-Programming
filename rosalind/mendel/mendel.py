f = open('rosalind_tree.txt')
pop = []
for line in f:
    pop.append(line)

params = pop[0].split(' ')
print (params)

homo_dom = int(params[0])
hetero = int(params[1])
homo_rec = int(params[2])
sum = homo_dom + hetero + homo_rec

print (sum)

homo_dom_select = (homo_dom/sum * (homo_dom-1)/(sum-1) * 1) + \
                  (homo_dom/sum * (hetero)/(sum-1) * 1) + \
                  (homo_dom/sum * (homo_rec)/(sum-1) * 1)

hetero_select =   (hetero/sum * (homo_dom)/(sum-1) * 1) + \
                  (hetero/sum * (hetero-1)/(sum-1) * 0.75) + \
                  (hetero/sum * (homo_rec)/(sum-1) * 0.5)

homo_rec_select = (homo_rec/sum * (homo_dom)/(sum-1) * 1) + \
                  (homo_rec/sum * (hetero)/(sum-1) * 0.5) + \
                  (homo_rec/sum * (homo_rec-1)/(sum-1) * 0)
prop = homo_dom_select + hetero_select + homo_rec_select

print(prop)
