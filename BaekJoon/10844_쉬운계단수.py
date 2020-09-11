import sys
n = int(sys.stdin.readline())
dp = [[0,1,2,3,4,5,6,7,8,9] for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
answer = sum(dp[n])
print(answer%1000000000)
