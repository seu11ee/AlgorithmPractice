def solution(stones, k):
    r = max(stones)
    l = min(stones)
    answer = l
    while l<=r:
        m = (l+r)//2
        temp = 0
        for i in range(len(stones)):
            if stones[i] - m >= 0:
                temp = 0
                continue
            else:
                temp += 1
                if temp == k:
                    break
        if temp < k:
            answer = m
            l = m + 1
        else:
            r = m - 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))