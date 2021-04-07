from sys import stdin

n = int(stdin.readline())
order = stdin.readline().split()
dx = [0,1,0,-1]
dy = [-1,0,1,0]
orderDict = {'U':0,
             'R':1,
             'D':2,
             'L':3
             }
start = [1,1]
for i in order:
    direction = orderDict[i]
    nx = start[0]+dx[direction]
    ny = start[1]+dy[direction]
    if nx <= n and nx > 0 and ny <= n and ny > 0:
        start = [nx,ny]
print(start[1],start[0])
