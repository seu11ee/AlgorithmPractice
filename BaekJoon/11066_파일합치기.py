'''
input:
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
'''
import sys

t = int(sys.stdin.readline())


#테스트케이스 수만큼 반복
for _ in range(t):
    k = int(sys.stdin.readline())
    memo = [[0 for _ in range(k)] for _ in range(k)]
    def dp(start, end):
        memo[start][end]
    pages = list(map(int,sys.stdin.readline().split()))
    for i in range(k-1):
        for j in range(i+1,k):
            pages[i]
