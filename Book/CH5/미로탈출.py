import sys
from collections import deque
graph = []
queue = deque([(0,0)])
dy = (-1,0,1,0)
dx = (0,1,0,-1)
n,m = map(int,sys.stdin.readline().split())

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
while queue:
    y,x = queue.popleft()
    if (y,x) == (n-1,m-1):
        print(graph[y][x])
        break
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 1 and not (ny,nx) == (0,0):
            graph[ny][nx] += graph[y][x]
            queue.append((ny,nx))

