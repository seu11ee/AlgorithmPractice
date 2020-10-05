import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
if n == 1:
    print(1)
else:
    for k in range(n):
        dp[k] = 1
        for i in range(k):
            if a[i] < a[k]:
                dp[k] = max(dp[k],dp[i]+1)

    print(max(dp))