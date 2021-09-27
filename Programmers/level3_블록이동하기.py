from collections import deque

HORIZONTAL = 0
VERTICAL = 1


def check_boundary(point, board):
    x, y = point[0], point[1]
    n = len(board)
    if -1 < x < n and -1 < y < n:
        if board[y][x] == 0:
            return True
    return False


def rotate_robot(first, axis, direction, clockwise, board):
    fail = (-1,-1,-1)
    if direction == HORIZONTAL:
        second = (first[0] + 1, first[1])
        if axis == first:
            if clockwise:
                block = (axis[0] + 1, axis[1] + 1)
            else:
                first = (first[0],first[1]-1)
                block = (axis[0] + 1, axis[1] - 1)
        else:
            if clockwise:
                first = (first[0]+1,first[1]-1)
                block = (axis[0] - 1, axis[1] - 1)
            else:
                first = second
                block = (axis[0] - 1, axis[1] + 1)
        second = (first[0], first[1] + 1)
    else:
        second = (first[0], first[1]+1)
        if axis == first:
            if clockwise:
                first = (first[0] - 1, first[1])
                block = (axis[0] - 1, axis[1] + 1)
            else:
                block = (axis[0] + 1, axis[1] + 1)
        else:
            if clockwise:
                first = second
                block = (axis[0] + 1, axis[1] - 1)
            else:
                first = (first[0] - 1, first[1] + 1)
                block = (axis[0] - 1, axis[1] - 1)

        second = (first[0]+1, first[1])
    if not (check_boundary(block, board) and check_boundary(first, board) and check_boundary(second, board)):
        return fail

    return first, second, 1 - direction


def solution(board):
    answer = 0
    n = len(board)
    visit = set()
    second_x = [1, 0]
    second_y = [0, 1]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = deque()
    queue.append(((0, 0), HORIZONTAL, 0))
    visit.add(((0, 0), HORIZONTAL))
    while queue:
        first, direction, cost = queue.popleft()

        second = (first[0] + second_x[direction], first[1] + second_y[direction])
        if (n - 1, n - 1) in (first, second):
            answer = cost
            break
        for i in range(4):
            next_first = (first[0] + dx[i], first[1] + dy[i])
            if (next_first, direction) not in visit:
                next_second = (next_first[0] + second_x[direction], next_first[1] + second_y[direction])
                if check_boundary(next_first,board) and check_boundary(next_second,board):
                    queue.append((next_first, direction, cost + 1))
                    visit.add((next_first,direction))

        for axis in [first, second]:
            for clockwise in [True, False]:
                next_first, next_second, next_dir = rotate_robot(first, axis, direction, clockwise, board)
                if (next_first,next_second,next_dir) == (-1,-1,-1):
                    continue
                if (next_first, next_dir) not in visit:
                    queue.append((next_first, next_dir, cost + 1))
                    visit.add((next_first,next_dir))

    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))