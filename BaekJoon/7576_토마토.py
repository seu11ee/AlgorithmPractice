#BFS
import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
tomato = [[-1 for _ in range(m+2)] for _ in range(n+2)]
visited = [[0 for _ in range(m+2)] for _ in range(n+2)]

for i in range(1,n+1):
    tomato[i][1:m+1] = map(int,sys.stdin.readline().split())


queue = deque()
for i in range(1,n+1):
    for j in range(1,m+1):
        if tomato[i][j] == 1:
            queue.append((i,j))

while(queue):
    now = queue.popleft()
    i,j = now[0],now[1]
    #오른쪽
    if tomato[i][j+1] == 0:
        tomato[i][j+1] = 1
        if visited[i][j+1] == 0:
            visited[i][j + 1] = visited[i][j] + 1
            queue.append((i,j+1))
    #아래
    if tomato[i+1][j] == 0 :
        tomato[i+1][j] = 1
        if visited[i+1][j] == 0:
            visited[i+1][j] = visited[i][j] + 1
            queue.append((i+1, j))
    #왼쪽
    if tomato[i][j-1] == 0:
        tomato[i][j-1] = 1
        if visited[i][j-1] == 0:
            visited[i][j - 1] = visited[i][j] + 1
            queue.append((i,j-1))
    #위
    if tomato[i-1][j] == 0 :
        tomato[i-1][j] = 1
        if visited[i-1][j] == 0:
            visited[i-1][j] = visited[i][j] + 1
            queue.append((i-1, j))

maxx = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if maxx<visited[i][j]:
            maxx = visited[i][j]


answer = maxx
for i in tomato:
    if 0 in i:
        answer = -1
        break
print(answer)






