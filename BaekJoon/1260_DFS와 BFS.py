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
            #단독그래프인지 검사해주어야하암
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
            visited[now] = True
            printStr += str(now) + " "
            if graph[now] != [-1]:
                graph[now].sort()

                for neighbor in graph[now]:
                    queue.append(neighbor)
    return printStr
print(dfs(V)+"\n"+bfs(V))
