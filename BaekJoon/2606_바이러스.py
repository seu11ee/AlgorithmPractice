#DFS/BFS
import sys
from collections import deque

nCom = int(sys.stdin.readline())
nNet = int(sys.stdin.readline())
comList = [0 for _ in range(nCom+1)]
visited = comList[:]

for _ in range(nNet):
    n1, n2 = map(int,sys.stdin.readline().split())
    if comList[n1] == 0:
        comList[n1] = [n2]
    else:
        comList[n1].append(n2)
    if comList[n2] == 0:
        comList[n2] = [n1]
    else:
        comList[n2].append(n1)


def BFS(graph,visit):
    queue = deque()
    queue.append(1)
    while(queue):
        now = queue.popleft()
        for neighbor in graph[now]:
            if visit[neighbor] == 0 :
                queue.append(neighbor)
                visit[neighbor] = 1
    return visit.count(1)
print(BFS(comList,visited)-1) #1번 컴퓨터 빼고 세야함

