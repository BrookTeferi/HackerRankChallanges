from itertools import combinations
collections=input().split()
s=collections[0]
n=int(collections[1])

for i in range(1,n+1):
  for j in combinations(sorted(s),i):
      print("".join(j))