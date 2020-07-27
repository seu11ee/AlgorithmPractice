from collections import deque

def solution(priorities, location):

    answer = 0
    q = deque(enumerate(priorities))


    while (q):
        isPrint = True
        now = q.popleft()
        for i in q:
            if i[1]> now[1]:
                q.append(now)
                isPrint = False
                break
        if isPrint:
            answer +=1
            if now[0] == location:
                return answer



print(solution([2,1,3,2],2))