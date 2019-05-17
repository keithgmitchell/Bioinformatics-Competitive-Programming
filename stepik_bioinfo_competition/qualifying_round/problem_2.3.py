
import math
from scipy.stats import poisson, binom



def get_coverage(readlength, number, genome_length):
    coverage = (readlength * number)/genome_length
    return coverage



# L, n, p, k (length_gen, read_length, error, number)
rl = 3
num = 4
len = 10
coverage = get_coverage(rl, num, len)
max_no_cov = len-rl
print (rl,num,len,max_no_cov)

sum = 0
# for i in range(rl,len):
#     print (i)
#     sum += 0.75 * 1/(num) * (len-i)
#     print (sum)

for num_cov in range(rl, len+1):

    print ((len-num_cov), max_no_cov, binom.pmf((len-num_cov),max_no_cov,0.5))
    sum += 0.75 * (len-num_cov) * (binom.pmf((len-num_cov),max_no_cov,0.5))
    print ('---------')
    print (num_cov,sum)
    print (' ')
print (sum)