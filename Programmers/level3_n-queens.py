def n_queens(x, visit, board):
    n = len(board)
    if x == n:
        return 1
    cnt = 0
    for i in range(n):
        board[i][x] = 1
        if visit[i] == 0:
            if not is_attacked(x, i, n, board):
                visit[i] = 1
                cnt += n_queens(x + 1,visit, board)
                visit[i] = 0
        board[i][x] = 0
    return cnt


def is_attacked(x, y, n, board):
    # 대각선 검사
    i = -min(x, y)
    while x + i < n and y + i < n:
        if i == 0:
            i += 1
            continue
        if board[y + i][x + i] == 1:
            return True
        i += 1
    i = min(y+1, n - 1 - x)
    while x + i > -1 and y - i < n:
        if i == 0:
            i -= 1
            continue
        if board[y - i][x + i] == 1:
            return True
        i -= 1
    return False


def solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    visit = [0 for _ in range(n)]
    answer = n_queens(0, visit, board)

    return answer

print(solution(4))