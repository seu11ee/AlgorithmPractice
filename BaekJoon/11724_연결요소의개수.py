import sys
import collections
N,M = map(int,sys.stdin.readline().split())
graph = [[-1]]*(N+1) #인덱스 1~N번 노드에 인접한 노드 써준다 -1이면 인접 없음 단독그래프
graph[0] = []
if M == 0:
    print(N)
else:
    cnt = 0
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
    #cnt += graph.count([-1])

    #BFS탐색시작
    queue = collections.deque()
    visited = [False]*(N+1)

    for i in range(1,N+1):
        #print(i,visited)
        if visited[i] == False:
            queue.append(i)
            cnt += 1
            #print(cnt)
        else:continue

        while(queue):
            now = queue.popleft()
            visited[now] = True
            graph[now].sort()
            if graph[now][0] != -1:

                for neighbor in graph[now]:
                    if not(visited[neighbor]):
                        visited[neighbor] = True
                        queue.append(neighbor)

    print(cnt)
