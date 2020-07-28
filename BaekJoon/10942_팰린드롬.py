import sys

N = int(sys.stdin.readline())
num = [0]
num.extend(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
memo = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(0)
    memo.append(temp)

for i in range(1,N+1):
    memo[i-1][i-1] = 1
for i in range(1,N):
    if num[i] == num[i+1]:
        memo[i-1][i] = 1
for i in range(3,N+1):
    for j in range(1,N-i+2):
        k = i + j - 1
        if (num[j] == num[k] and memo[j][k-2]):
            memo[j-1][k-1] = 1
for _ in range(M):
    S,E = map(int,sys.stdin.readline().split())
    print(memo[S-1][E-1])




