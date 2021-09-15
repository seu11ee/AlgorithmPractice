STAR = "*"
BLANK = " "
N = int(input())
stars = [[BLANK for _ in range(N)] for _ in range(N)]


def draw_stars(x, y, n, board):
    if n == 1:
        board[y][x] = STAR
    else:
        space = n//3
        flag = 1
        for _ in range(2):
            for i in range(3):
                board = draw_stars(x, y, n // 3, board)
                x += flag * space
            x -= flag * space
            y += flag * space
            board = draw_stars(x, y, n // 3, board)
            y += flag * space
            flag *= -1

    return board


for line in draw_stars(0, 0, N, stars):
    for star in line:
        print(star, end = '')
    print()

