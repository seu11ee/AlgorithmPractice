import sys
N, M = map(int,sys.stdin.readline())
a = [[0]*(M+1)]*[N+1]
d = [[0]*(M+1)]*[N+1]
#배열 인덱스 1,1부터 시작
for n in range(1,N+1):
    a[n] = list(map(int,sys.stdin.readline().split()))
for i in range(1,N+1):
    for j in range(1,M+1):



