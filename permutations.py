from itertools import permutations

#method 1
s,k = input().split()

words = list(permutations(s,int(k)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')

#method 2
for i in permutations(sorted(s),int(k)):
    print("".join(i))

