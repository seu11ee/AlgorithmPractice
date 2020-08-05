import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
link = []
for _ in range(N+1):
    link.append([0] * (N+1))
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    link[v1][v2], link[v2][v1] = 1, 1
def dfs(v):
    #global visited
    visited = [0] * (N+1)
    seq = [v]
    res = []
    while seq:
        p = seq.pop()
        if not visited[p]:
            visited[p] = 1
            res.append(str(p))
            for i in range(N, 0, -1):
                if link[p][i]:
                    seq.append(i)
    return res
def bfs(v):
    #global visited
    visited = [0] * (N+1)
    seq = deque([v])
    res = []
    while seq:
        p = seq.popleft()
        if not visited[p]:
            visited[p] = 1
            res.append(str(p))
            for i in range(1, N+1):
                    if link[p][i]:
                        seq.append(i)
    return res
sys.stdout.write(' '.join(dfs(V)) + "\n")
sys.stdout.write(' '.join(bfs(V)))
