def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    flag = True
    dx = (0,1,1,0)
    dy = (0,0,1,1)
    while flag:
        flag = False
        check = set()
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == "-":
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    flag = True
                    for k in range(4):
                        check.add((i+dy[k],j+dx[k]))
        answer += len(check)
        for x,y in check:
            board[x][y] = "-"
        for i in range(n):
            temp_2 = list(filter(lambda x:x != "-",board[i]))
            temp_1 = ["-"]*(m-len(temp_2))
            temp_1.extend(temp_2)
            board[i] = temp_1
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))