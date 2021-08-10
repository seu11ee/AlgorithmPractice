import heapq
from collections import deque


def solution(jobs):
    time = 0
    queue = []
    n = len(jobs)
    times = []
    prev = -1
    while (len(times)<n):
        # print(queue)
        # 새 작업 추가
        for job in jobs:
            if prev < job[0] <= time:
                heapq.heappush(queue, [job[1], job[0]])
        if not queue:
            time += 1
            continue
        remaining, start = heapq.heappop(queue)
        prev = time

        time += remaining
        times.append(time - start)

    # print(times)
    return sum(times) // n

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))