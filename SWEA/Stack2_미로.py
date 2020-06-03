'''NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.

13101

10101

10101

10101

10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로,
1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.'''

#개모르겠음 아아아아

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
STOP = 4
T = int(input())
for t in range(1,T+1):
    N = int(input())
    possible = 0
    maze = []
    stack = []
    dir = [[0]*N]*N

    for _ in range(N):
        maze.append(list(map(int,list(input()))))
    #print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                startIndex = (i,j)
                break
    stack.append(startIndex)
    now = startIndex
    count=0
    while(True):
        print(stack)
        x = now[1]
        y = now[0]
        count+=1
        if maze[y][x]==3:
            possible = 1
            break
        if dir[y][x]==UP:
            print("up")
            dir[y][x]+=1 #다음가야할방향 하나 증가 시켜
            if 0<y:
                if maze[y-1][x]==0:
                    now = (y-1,x)
                    stack.append(now)
            else:
                continue
        elif dir[y][x] == RIGHT:
            print("right")
            dir[y][x]+= 1
            if x<N-1:
                if maze[y][x+1] == 0:
                    now = (y, x + 1)
                    stack.append(now)
                else:
                    continue
        elif dir[y][x] == DOWN:
            print("down")
            dir[y][x]+=1
            if y<N-1:
                if maze[y+1][x] == 0:
                    now = (y + 1, x)
                    stack.append(now)
            else: continue
        elif dir[y][x] ==LEFT:
            print("left")
            dir[y][x]+=1
            if x>0:
                if maze[y][x-1]==0:
                    now = (y,x-1)
                    stack.append(now)
            else:
                continue
        else:
            stack.pop()
            now = stack.pop()

    print("#%d %d"%(t,possible))







