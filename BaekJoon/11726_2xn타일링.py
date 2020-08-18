import sys
n = int(sys.stdin.readline())
memo = [ 0 for _ in range(n+3)]
memo[1] = 1
memo[2] = 2
i=1
while(i<=n):
    if memo[n]!=0:
        print(memo[n]%10007)
        break
    else:
        memo[i+2] = memo[i]+memo[i+1]
        i+=1

