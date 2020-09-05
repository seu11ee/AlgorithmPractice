import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
maze = [[-1 for _ in range(m+2)] for _ in range(n+2)]
visited = [[[0,0] for _ in range(m+2)] for _ in range(n+2)] #3차원 visited 리스트
dx = [0,1,0,-1] #오아왼위
dy = [1,0,-1,0]
queue = deque()
# broken = (0,0)
for i in range(1,n+1):
    maze[i][1:m+1] = map(int,list(sys.stdin.readline().rstrip()))

queue.append((1,1,0))
answer = []
visited[1][1] = [1,1]
while queue:

    x, y, flag = queue.popleft()

    if x == n and y == m:
        if flag == 0:
            answer.append(visited[n][m][0])
        else:
            answer.append(visited[n][m][1])
    # blocked = True
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        #원래뚫린길
        if maze[nx][ny] == 0:
            #벽안부순/부순경로
            if visited[nx][ny][flag] == 0:
                queue.append((nx, ny, flag))
                visited[nx][ny][flag] = visited[x][y][flag] + 1
        #벽
        elif maze[nx][ny] == 1:
            #아직 부순적 없음
            if flag == 0:
                if visited[nx][ny][1] == 0:
                    queue.append((nx, ny,1))
                    visited[nx][ny][1] = visited[x][y][0] + 1

length = len(answer)
if length == 0 :
    print(-1)
else:
    print(min(answer))





'''
반례
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
'''

