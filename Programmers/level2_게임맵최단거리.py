from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def solution(maps):
    answer = -1
    cnt = 0
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    visit = [[False for _ in range(m)] for _ in range(n)]
    queue.append([0, 0, 1])
    visit[0][0] = True
    while queue:
        y, x, cnt = queue.popleft()

        if (y, x) == (n - 1, m - 1):
            answer = cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny and ny < n and 0 <= nx and nx < m:
                if maps[ny][nx] == 1 and visit[ny][nx] == False:
                    queue.append([ny, nx, cnt + 1])
                    visit[ny][nx] = True

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11