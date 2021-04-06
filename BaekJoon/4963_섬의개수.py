from sys import stdin
from collections import deque
w,h = -1, -1
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]
while(True):
    w,h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    island = deque()
    for y in range(h):
        x = 0
        for i in map(int, stdin.readline().split()):
            if i == 1:
                island.append((x,y))
            x += 1
    cnt = 0
    while(island):
        x,y = island.pop()
        stack = deque()
        stack.append((x,y))
        visited = [[0 for _ in range(w)] for _ in range(h)]
        while(stack):
            x,y = stack.pop()
            visited[y][x] = 1
            if (x,y) in island:
                island.remove((x,y))
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) in island:
                    stack.append((nx, ny))

        cnt += 1
    print(cnt)













