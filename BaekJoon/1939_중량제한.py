import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
bridges = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    bridges[a-1].append([b-1,c])
    bridges[b-1].append([a-1,c])
start,end = map(int,input().split())

left = 1
right = 1000000000
mid = (left + right) // 2


def bfs(x):
    queue = deque()
    queue.append(start - 1)
    visit = set()
    visit.add(start-1)
    while queue:
        now = queue.popleft()
        if now == end - 1:
            return True
        for idx, limit in bridges[now]:
            if idx not in visit:
                if limit >= x:
                    queue.append(idx)
                    visit.add(idx)

    return False


def binary_search(left,right):
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


print(binary_search(left,right))