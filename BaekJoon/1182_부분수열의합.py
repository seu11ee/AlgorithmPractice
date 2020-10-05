from itertools import combinations
import sys
n,s = map(int,sys.stdin.readline().split())
sequence = list(map(int,sys.stdin.readline().split()))

ans = 0
for i in range(1,n+1):
    for com in combinations(sequence,i):
        if sum(com)==s:
            ans += 1
print(ans)

