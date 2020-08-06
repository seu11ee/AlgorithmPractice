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
maze = [[-1] for _ in range(N+1)]
print(maze)

#print(maze)
for n in range(1,N+1):
    input_ = stdin.readline().rstrip("\n") #스트링을 리스트로 만들 때 줄바꿈 문자도 포함되므로 없애야함
    maze[n].extend(list(map(int,list(input_))))
for item in maze:
    print(item)
print(maze[1][1])
print(maze[N][M])


dest = (N,M)
start = (1,1)
count = 1
queue = deque()
queue.append(start)
now = queue.popleft()


visited=[]

