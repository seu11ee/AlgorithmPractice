#미로 탐색
#BFS
'''N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.'''

from sys import stdin
from collections import deque
N,M=map(int,stdin.readline().split())
maze = [[0 for _ in range(M+2)] for _ in range(N+2)]
visited = [[0 for _ in range(M+2)] for _ in range(N+2)]
for i in range(N+1):
    visited[i][0] = True
    visited[i][-1] = True
for i in range(M+1):
    visited[0][i] = True
    visited[-1][i] = True

for n in range(1,N+1):
    input_ = stdin.readline().rstrip("\n") #스트링을 리스트로 만들 때 줄바꿈 문자도 포함되므로 없애야함
    maze[n][1:M+1] = list(map(int,list(input_)))

q = deque()
q.append((1,1))

while(q):
    x,y = q.popleft()

    
    if (x,y) == (N, M):
        print(visited[x][y]+1)
        break
    #왼
    if maze[x-1][y]==1:
        if visited[x-1][y]==0:
            q.append((x-1,y))
            visited[x-1][y] = visited[x][y] + 1
    #아래
    if maze[x][y+1]==1:
        if not visited[x][y+1]:
            q.append((x,y+1))
            visited[x][y+1] = visited[x][y] + 1
    #오
    if maze[x+1][y]==1:
        if not visited[x+1][y]:
            q.append((x+1,y))
            visited[x + 1][y] = visited[x][y] + 1
    #위
    if maze[x][y-1]==1:
        if not visited[x][y-1]:
            q.append((x,y-1))
            visited[x][y - 1] =  visited[x][y] + 1

