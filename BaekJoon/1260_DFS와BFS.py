'''
import sys
import collections
N,M,V = map(int,sys.stdin.readline().split())
graph=[]
for _ in range(N+1):
    graph.append([-1])
#print(graph)
#인덱스 1~N번 노드에 인접한 노드 써준다 -1이면 인접 없음 단독그래프
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
#DFS탐색시작
def dfs(v):
    stack = list()
    visited = [False]*(N+1)
    stack.append(v)
    printStr = ""

    while(stack):
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            printStr += str(now) + " "
            length = len(graph[now])
            if graph[now] != [-1]:

                graph[now].sort(reverse = True)
                for neighbor in graph[now]:
                    stack.append(neighbor)

    return printStr

#BFS탐색시작
def bfs(v):
    queue = collections.deque()
    visited = [False]*(N+1)
    queue.append(v)
    printStr = ""
    while(queue):
        now = queue.popleft()
        if not visited[now]:
            visited[now] = True2
            printStr += str(now) + " "
            if graph[now] != [-1]:
                graph[now].sort()

                for neighbor in graph[now]:
                    queue.append(neighbor)
    return printStr
print(dfs(V)+"\n"+bfs(V))
'''

from collections import deque
from sys import stdin 

n, m, v = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, stdin.readline().split())
    if n2 not in graph[n1]:
        graph[n1].append(n2)
        graph[n2].append(n1)
stack = deque()
graph2 = graph[:]
stack.append(v)

while(stack):
    now = stack.pop()

    if visited[now] == 0:
        print(now, end = " ")
    if graph2[now] == []:
        continue
    visited[now] = 1
    graph2[now].sort(reverse = True)
    for neighbor in graph2[now]:
        if visited[neighbor] == 0:
            stack.append(neighbor)

visited = [0 for _ in range(n+1)]

queue = deque()
queue.append(v)
visited[v] = 1
print()

while(queue):
    now = queue.popleft()
    print(now, end = " ")
    if graph[now] == []:
        continue
    graph[now].sort()
    for neighbor in graph[now]:
        if visited[neighbor] == 0:
            queue.append(neighbor)
            visited[neighbor] = 1






