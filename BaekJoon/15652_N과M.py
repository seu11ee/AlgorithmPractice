import sys
from itertools import combinations_with_replacement #중복조합
N,M = map(int,sys.stdin.readline().split())
list1 = range(1,N+1)
answer = list(map(list,combinations_with_replacement(list1,M)))
for i in answer:
    for j in i:
        print(j,end =" ")
    print()

