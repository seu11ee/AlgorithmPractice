import heapq  # 우선순위 큐 구현을 위함
from collections import defaultdict

def dijkstra(graph, start,n):
    distances = {i: float('inf') for i in range(n)}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances


def solution(n, s, a, b, fares):
    answer = []
    graph = defaultdict(dict)
    for fare in fares:
        graph[fare[1] - 1][fare[0] - 1] = fare[2]
        graph[fare[0] - 1][fare[1] - 1] = fare[2]
    sToX = dijkstra(graph, s - 1,n)
    aToX = dijkstra(graph, a - 1,n)
    bToX = dijkstra(graph, b - 1,n)
    for x in range(n):
        answer.append(sToX[x] + aToX[x] + bToX[x])

    return min(answer)

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))