from collections import defaultdict
from collections import deque
import itertools
import copy
def solution(board, r, c):
    answer = []
    card_locations = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if not board[i][j] == 0:
                card_locations[board[i][j]].append([j,i])
    keys = card_locations.keys()
    n = len(keys)
    #가능한 모든 방문순서 만들기
    orders = []
    two_cards_order = tuple(itertools.product(range(2),repeat = n))
    for order in itertools.permutations(keys):
        for t in two_cards_order:
            temp = []
            for i in range(n):
                temp.append(card_locations[order[i]][t[i]])
                temp.append(card_locations[order[i]][1-t[i]])
            orders.append(temp)
    for order in orders:
        cost = 0
        start_x,start_y = c,r
        copy_board = copy.deepcopy(board)
        for dest_x,dest_y in order:
            cost += get_min_distance(start_x,start_y,dest_x,dest_y,copy_board)
            copy_board[dest_y][dest_x] = 0
            start_x,start_y = dest_x,dest_y
        answer.append(cost)
    return min(answer) + n*2

def get_min_distance(x1,y1,x2,y2,board):
    cost = 0
    queue = deque()
    visit = set()
    queue.append([x1,y1,cost])
    visit.add((x1,y1))
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    while queue:
        x,y,cost = queue.popleft()
        if (x,y) == (x2,y2):
            return cost
        for i in range(4):
            # ctrl 누르고 이동
            mx, my = x, y
            while True:
                mx += dx[i]
                my += dy[i]
                if not ((-1 < mx and mx < 4) and (-1 < my and my < 4)):
                    mx -= dx[i]
                    my -= dy[i]
                    break
                if not board[my][mx] == 0:
                    break
            if (mx, my) not in visit:
                if (mx, my) == (x2, y2):
                    return cost+1
                queue.append([mx, my, cost + 1])
                visit.add((mx, my))
            nx = x + dx[i]
            ny = y + dy[i]

            if -1<nx<4 and -1<ny<4 and (nx,ny) not in visit:
                if (nx, ny) == (x2, y2):
                    return cost+1
                queue.append([nx,ny,cost+1])
                visit.add((nx,ny))

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))

