'''
기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
'''
COLUMN = 0
BEAM = 1
REMOVE = 0
ADD = 1
def solution(n, build_frame):
    answer = []
    board = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for x,y,a,b in build_frame:
        #구조물 삭제
        if b == REMOVE:
            board[y][x].remove(a)
            if not check_rule(x,y,a,b,board):
                board[y][x].append(a)
        #구조물 설치
        elif b == ADD:
            board[y][x].append(a)
            if not check_rule(x,y,a,b,board):
                board[y][x].remove(a)
    for i in range(0,n+1):
        for j in range(0,n+1):
            if len(board[j][i]) == 2:
                answer.append([i,j,0])
                answer.append([i,j,1])
            elif len(board[j][i]) == 1:
                answer.append([i,j,board[j][i][0]])
    return answer
def check_rule(x,y,a,b,board):
    if b == ADD:
        if check_safety(x,y,a,board):
            return True
        return False
    elif b == REMOVE:
        #기둥 제거
        if a == COLUMN:
            #바로 위 기둥
            if check_exist(x,y+1,COLUMN,board) and not check_safety(x,y+1,COLUMN,board):
                return False
            #왼쪽에 보
            if check_exist(x-1,y+1,BEAM,board) and not check_safety(x-1,y+1,BEAM,board):
                return False
            #오른쪽에 보
            if check_exist(x,y+1,BEAM,board) and not check_safety(x,y+1,BEAM,board):
                return False
        #보 제거
        elif a == BEAM:
            #왼쪽 보에 대한 검사
            if check_exist(x-1,y,BEAM,board) and not check_safety(x-1,y,BEAM,board):
                return False
            #오른쪽 보 검사
            if check_exist(x+1,y,BEAM,board) and not check_safety(x+1,y,BEAM,board):
                return False
            #왼쪽 기둥 검사
            if check_exist(x,y,COLUMN,board) and not check_safety(x,y,COLUMN,board):
                return False
            #오른쪽 기둥 검사
            if check_exist(x+1,y,COLUMN,board) and not check_safety(x+1,y,COLUMN,board):
                return False
        return True

def check_exist(x,y,a,board):
    n = len(board)-1
    if x < 0 or x > n or y < 0 or y > n:
        return False
    if a in board[y][x]:
        return True
def check_safety(x,y,a,board):
    #보에 대한 규칙 검사
    if a == BEAM:
        #한쪽 끝 부분이 기둥 위에 있거나
        if COLUMN in board[y-1][x] or COLUMN in board[y-1][x+1]:
            return True
        #양쪽끝이 다른 보와 연결되어 있거나
        if BEAM in board[y][x-1] and BEAM in board[y][x+1]:
            return True
        return False
    #기둥에 대한 규칙 검사
    elif a == COLUMN:
        #바닥에 있거나
        if y == 0:
            return True
        #다른 기둥 위에 있거나
        if COLUMN in board[y-1][x]:
            return True
        #보의 한쪽 끝 위에 있거나
        if BEAM in board[y][x-1] or BEAM in board[y][x]:
            return True
        return False
print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))