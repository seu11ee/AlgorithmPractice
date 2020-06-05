#메모리 초과

import sys
from itertools import permutations
N = int(sys.stdin.readline())
l = list(permutations(range(1,N+1),N))

num = tuple(map(int,sys.stdin.readline().rstrip().split()))

index = l.index(num)
if num == tuple(range(N,0,-1)):
    print(-1)
else:
    for i in range(N):
        print(l[index+1][i],end = " ")