def solution(citations):
    n = len(citations)
    citations.sort(reverse = True)
    answer = 0
    for i in range(n):
        m = min(citations[i],i+1)
        if answer < m:
            answer = m

    return answer
print(solution([3,0,6,1,5]))
