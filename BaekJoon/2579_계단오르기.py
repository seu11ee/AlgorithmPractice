import sys

n = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(n)]

dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0][1] = stairs[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + stairs[i]
    dp[i][2] = dp[i-1][1] + stairs[i]

print(max(dp[n-1][1],dp[n-1][2]))

