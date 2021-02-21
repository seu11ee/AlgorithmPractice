from sys import stdin

n = int(stdin.readline())

pinary = [[0,0] for _ in range(n)]

pinary[0][1] = 1

for i in range(1,n):
    pinary[i][0] = pinary[i-1][0]+pinary[i-1][1]
    pinary[i][1] = pinary[i-1][0]

print(pinary[n-1][0]+pinary[n-1][1])