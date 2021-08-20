import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline
n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [ INF for _ in range(n+1)]
visit = set()
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
distance[c] = 0
q = []
heapq.heappush(q,(0,c))
while q:
    dist,now = heapq.heappop(q)
    if now in visit:
        continue
    visit.add(now)
    for i in graph[now]:
        cost = distance[now]+i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
cnt = 0
time = -1
for i in distance:
    if i == INF:
        continue
    cnt += 1
    if time < i :
        time = i
print(cnt-1,time)