from collections import deque




T = int(input())

for t in range(1,T+1):
    V,E = map(int,input().split())
    graph = []
    for _ in range(V+1): #Graph 초기화
        graph.append([])
    for _ in range(E):
        temp = tuple(map(int,input().split()))
        graph[temp[0]].append(temp[1]) #Setting Graph
        graph[temp[1]].append(temp[0])
    S,G = map(int,input().split())
    queue = deque()
    visited = [False] * (V + 1)
    queue.append(S)
    count=0 #count 어떻게 세지?
    answer = 0
    while (queue):
        now = queue.popleft()
        if now == G:
            answer = count
            break
        visited[now] = True
        print("now",now)
        graph[now].sort()
        for neighbor in graph[now]:
            if not (visited[neighbor]):
                visited[neighbor] = True
                queue.append(neighbor)

    print("#%d %d"%(t,answer))