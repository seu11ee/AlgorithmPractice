from sys import stdin

n,m = map(int, stdin.readline().split())
y,x,d = map(int, stdin.readline().split())
mapList = []
visit = []
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(n):
    mapList.append(list(map(int,stdin.readline().split())))

cnt = 1
while(True):
    visit.append((y,x))
    flag = False
    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        nx = x+dx[d]
        ny = y+dy[d]
        if mapList[ny][nx] == 0 and (ny,nx) not in visit:
            cnt += 1
            x = nx
            y = ny
            flag = True
            break
    if not flag:
        nx = x - dx[d]
        ny = y - dy[d]
        if (ny,nx) in visit:
            break
        else:
            x = nx
            y = ny
            cnt += 1
print(cnt)