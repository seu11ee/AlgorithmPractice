from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]

#그래프 구조 생성
for _ in range(n-1):
    node1,node2 = map(int,stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

#BFS탐색시작
queue = deque()
visited = [False for _ in range(n+1)]
parents = [0 for _ in range(n+1)]
queue.append(1)

while(queue):
    now = queue.popleft()
    visited[now] = True
    graph[now].sort()
    for neighbor in graph[now]:
        if not(visited[neighbor]):
            visited[neighbor] = True
            parents[neighbor] = now
            queue.append(neighbor)
for i in range(2,n+1):
    print(parents[i])
