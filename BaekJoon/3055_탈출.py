from sys import stdin
from collections import deque

R, C =map(int,stdin.readline().split())
maze = [[0 for _ in range(C)] for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
water = [[0] for _ in range(R*C)]
dx = (1,0,-1,0)
dy = (0,-1,0,1)
queue = deque()
temp = []
for r in range(R):
    cList = list(stdin.readline().rstrip())
    for c in range(len(cList)):
        if cList[c] == "D":
            D = (r,c)
        elif cList[c] == "S":
            S = (r,c)
        elif cList[c] == "*":
            temp.append((r,c))
        maze[r][c] = [cList[c],0]
water[0] = temp
# visit = [S]
answer = "KAKTUS"
queue.append(S)
visit[S[0]][S[1]] = 1
def makeWater(i):
    if water[i-1] == [0]:
        makeWater(i-1)
    else:
        temp = water[i-1][:]
        for w in water[i-1]:
            x = w[1]
            y = w[0]
            for j in range(4):
                wx = x + dx[j]
                wy = y + dy[j]
                if 0 <= wx and wx < C and 0 <= wy and wy < R and (wy, wx) not in water[i-1] and maze[wy][wx] != "X" and (
                wy, wx) != D:
                    temp.append((wy,wx))

        water[i] = temp
        # print("dd",i,water)
while(queue):
    y,x = queue.popleft()
    # print((y,x))
    # print("water",water)
    # print("visit",visit)
    if (y,x) == D:
        answer = visit[y][x] - 1
        break
    cnt = visit[y][x]
    # print("cnt",cnt,water)
    if water[cnt] == [0]:
        makeWater(cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print("water",water)
        if 0 <= nx and nx < C and 0 <= ny and ny < R and visit[ny][nx] == 0 and (ny,nx) not in water[cnt] and maze[ny][nx] != "X":
            visit[ny][nx] = cnt + 1
            queue.append((ny,nx))

print(answer)




#
# def dfs(y,x,depth,water):
#     newWater = water[:]
#     global visit
#     print(visit)
#     if x < 0 or y < 0 or x >= C or y >= R:
#         return
#     if (y,x) == D:
#         print(depth)
#         exit()
#         return
#     for w in water:
#         wy,wx = w[0], w[1]
#         for i in range(4):
#             nwx = wx + dx[i]
#             nwy = wy + dy[i]
#             if 0 <= nwx and nwx < C and 0 <= nwy and nwy < R and maze[nwy][nwx] != "X" and maze[nwy][nwx] != "D" and (nwy,nwx) not in newWater:
#                 newWater.append((nwy,nwx))
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0 <= nx and nx < C and 0 <= ny and ny < R and (ny,nx) not in visit and (ny,nx) not in newWater and maze[ny][nx] != "X":
#             temp = visit[:]
#             visit.append((ny,nx))
#             dfs(ny,nx,depth+1,newWater)
#             visit = temp
#
# dfs(S[0],S[1],0,water)






