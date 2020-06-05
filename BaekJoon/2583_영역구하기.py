'''
MxN 크기의 직사각형에 주어진 좌표로 K개의 사각형을 그려서 빈부분의 개수와 그 넓이 구하는 문제
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다.
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고
차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이
전체를 채우는 경우는 없다.
'''
import sys

M,N,K = map(int,sys.stdin.readline().split()) #1차원이 x,
point = []
visited = [[False]*M]*N
rect = []
for n in range(N):
    rect.append([1])
    for m in range(M):
        rect[n].append(1)

print(visited)
print(rect)
for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    point.append([(x1,y1),(x2,y2)])
    for i in range(x1,x2):
        for j in range(y1,y2):
            print("x,y :",i,j)
            rect[i][j] = 0
    print(rect)

graph = dict()
for x in range(N):
    for y in range(M):

        if rect[x+1][y]:
            graph[(x,y)] = (x+1,y)
            graph[(x+1,y)] = (x,y)
        elif rect[x][y+1]:
            graph[(x,y)] = (x,y+1)
            graph[(x,y+1)] = (x,y)
print(graph)



