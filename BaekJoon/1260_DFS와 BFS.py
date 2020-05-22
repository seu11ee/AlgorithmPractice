'''N 정점의 개수 M 간선의 개수 V 탐색 시작 노드
일단 BFS만'''

import sys
import collections
N,M,V = map(int,sys.stdin.readline().split())
graph = [[-1]]*(N+1) #인덱스 1~N번 노드에 인접한 노드 써준다 -1이면 인접 없음 단독그래프

#그래프 구조 생성
for _ in range(M):
    n1,n2 = map(int,sys.stdin.readline().split())
    if graph[n1]==[-1]:
        graph[n1]=[n2]
    else:
        graph[n1].append(n2)
    if graph[n2]==[-1]:
        graph[n2]=[n1]
    else:
        graph[n2].append(n1)

'''DFS탐색시작'''

#BFS탐색시작
queue = collections.deque()
visited = [False]*(N+1)
queue.append(V)

while(queue):
    now = queue.popleft()
    visited[now] = True
    print(now,end=" ")
    graph[now].sort()
    for neighbor in graph[now]:
        if not(visited[neighbor]):
            visited[neighbor] = True
            queue.append(neighbor)





