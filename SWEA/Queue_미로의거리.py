T = int(input())
for t in range(1,T+1):
    def search(y,x,mazeList):
        temp_values = []
        try:
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i,j)==(0,0):
                        continue
                    if mazeList[y+i][x+i] == 0:
                        temp_values.append((x+i,y+i))
            return temp_values
        except IndexError:
            pass

    answer = 0
    N = int(input())
    maze = [[]]*N
    graph = dict()
    for i in range(N):
        temp = map(int,list(input()))
        maze[i].extend(temp)
    for i in range(N):
        for j in range(N):
            now = maze[i][j]
            if now == 3: #시작노드
                start = (j,i)
            elif now == 2: #도착노드
                end = (j,i)
            elif now == 0: #통로
                graph[(j,i)] = search(i,j,maze)
    print(graph)




    print("#%d %d"%(t,answer))