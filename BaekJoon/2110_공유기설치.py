#binary search
#공유기의 갯수가 많을수록 간격은 좁아지며, 반대로 공유기의 갯수가 적을수록 간격을 넓어진다.
#이분탐색 문제 -> 어떤 값을 타겟으로 잡고 이분탐색으로 찾아나갈 것인지 -> 그 값의 범위(start,end) 주로 최소 최대를 설정해 탐색 시
import sys

n,c = map(int,sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
def solution(distance):
    cnt = 1
    start = l[0]
    for i in range(1, n):
        if start + distance <= l[i]:
            cnt += 1
            start = l[i]
    return cnt

start,end = 1, l[-1] - l[0]

while start <= end:
    mid = (start + end) // 2

    if solution(mid) >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
