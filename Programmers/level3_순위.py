def solution(n, results):
    answer = 0
    graph  = [[0 for _ in range(n)] for _ in range(n)]
    WIN,LOSE = 1,-1
    for winner,loser in results:
        graph[winner-1][loser-1] = WIN
        graph[loser-1][winner-1] = LOSE
    printGraph(graph)
    print()
    for i in range(n):
        for j in range(n):
            if i==j or graph[i][j]==0:
                continue
            stack = [j]
            while stack:
                printGraph(graph)
                now = stack.pop()
                for k in range(n):
                    if graph[now][k] == graph[i][now] and graph[i][k] == 0:
                        graph[i][k] = graph[now][k]
                        stack.append(k)
        answer += checkRank(graph[i],i)
    print()
    printGraph(graph)
    return answer
def checkRank(record,me):
    l = len(record)
    for i in range(l):
        if record[i]==0 and not me == i:
            return 0
    return 1
def printGraph(graph):
    print("-"*10)
    for i in graph:
        print(i)
    print("-"*10)
# print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(3,[[3, 2], [2, 1]]))