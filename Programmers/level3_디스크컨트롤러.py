#실패 코드를 jobs를 시작 시간에 따라 오름차순 정렬 후 for문 탐색하다 break
import heapq
def solution(jobs):
    times = []
    time = 0
    queue = list()
    prev = -1
    jobs.sort()
    while(jobs or queue):
        for job in jobs[:]:
            if prev<job[0]<=time:
                heapq.heappush(queue,[job[1],job[0]])
                del(jobs[0])
            else:
                break
        if queue:
            amount,start = heapq.heappop(queue)
            prev = time
            time += amount
            times.append(time-start)
        else:
            time+=1
    return sum(times)//len(times)