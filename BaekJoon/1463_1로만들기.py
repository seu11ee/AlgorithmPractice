'''정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.'''
#Top-down 런타임에러남 ㅁㄹ겠. 재귀함수호출 최대값 초과
#Bottom-up으로
import sys
N = int(sys.stdin.readline())

def solve(n):
    if n == 1:
        return 0
    dp = [0 for _ in range(N + 1)]
    dp[1] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1]+1
        if i%2==0 and dp[i]>dp[i//2]+1:
            dp[i] = dp[i//2]+1
        if i%3==0 and dp[i]>dp[i//3]+1:
            dp[i] = dp[i//3]+1
    return dp[n]

print(solve(N))



