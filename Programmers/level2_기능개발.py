from collections import deque
def solution(progresses, speeds):
    q = deque(zip(progresses,speeds))
    answer = []
    while(q):
        for i in range(len(q)):
            q[i] = (q[i][0]+q[i][1],q[i][1])
        cnt = 0
        while(q):
            now = q.popleft()
            if now[0] < 100:
                q.appendleft(now)
                break
            cnt += 1
        if cnt > 0:
            answer.append(cnt)

    return answer
print(solution([93,30,55],[1,30,5]))