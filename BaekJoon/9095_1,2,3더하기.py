import sys
T = int(sys.stdin.readline())
def solution(N):
    if N==1:
        return 1
    elif N ==2:

        return solution(1)+1
    elif N == 3:
        return solution(2)+2
    else:
        return solution(N-1)+solution(N-2)+solution(N-3)


for _ in range(T):
    n = int(sys.stdin.readline())
    print(solution(n))

