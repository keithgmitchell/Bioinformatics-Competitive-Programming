# https://stackoverflow.com/a/18717762/7305166

def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer


from Bio import SeqIO

records = list(SeqIO.parse("rosalind_tree.txt", "fasta"))


for index in range(0,len(records)-1):
    print(longestSubstringFinder(str(records[index].seq), str(records[index+1].seq)))