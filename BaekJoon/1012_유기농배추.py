from sys import stdin
from collections import deque

dx = (0,1,0,-1)
dy = (-1,0,1,0)

def dfs(x,y):
    global answer
    stack = deque()
    stack.append((x,y))
    while(stack):
        x,y = stack.pop()
        if (x,y) in cabbage:
            cabbage.remove((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in cabbage:
                stack.append((nx,ny))
    answer += 1
    return answer
t = int(stdin.readline())
for _ in range(t):
    m,n,k = map(int,stdin.readline().split())
    cabbage = deque()
    for _ in range(k):
        x,y = map(int, stdin.readline().split())
        cabbage.append((x,y))

    answer = 0
    while(cabbage):
        x,y = cabbage.popleft()
        dfs(x,y)
    print(answer)

