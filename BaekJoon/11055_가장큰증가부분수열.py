import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
dp = a[:]

for i in range(n):
    for k in range(i):
        if a[k] < a[i]:
                dp[i] = max(dp[k]+a[i],dp[i])
print(max(dp))