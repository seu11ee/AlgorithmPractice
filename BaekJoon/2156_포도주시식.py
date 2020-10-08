import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
dp = [[0,0,0] for _ in range(n)]
dp[0] = [0,a[0],0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][2],dp[i-1][1],dp[i-1][0])
    dp[i][1] = dp[i-1][0]+a[i]
    dp[i][2] = dp[i-1][1]+a[i]

print(max(dp[-1]))
