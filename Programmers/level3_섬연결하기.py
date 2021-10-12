parent = []


def findParent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = findParent(parent[x])
        return parent[x]


def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    global parent
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    for a, b, cost in costs:
        if findParent(a) != findParent(b):
            answer += cost
            unionParent(a, b)
        else:
            continue

    return answer


print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))