import sys
sys.setrecursionlimit(300000)

answer = 0
def solution(a, edges):

    global answer

    sum_of_a = sum(a)
    adjacency_list = [[] for _ in range(len(a))]
    if not sum_of_a == 0:
        return -1
    for n, m in edges:
        adjacency_list[n].append(m)
        adjacency_list[m].append(n)
    visit = [False for _ in range(len(a))]
    visit[0] = True

    def dfs(now):
        global answer
        for next in adjacency_list[now]:
            if not visit[next]:
                visit[next] = True
                child = dfs(next)
                a[now] += child
                answer += abs(child)
        return a[now]
    dfs(0)
    return answer


print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))