CLOCKWISE = 1
ANTICLOCKWISE = -1
from itertools import permutations

def solution(n,weak,dist):
    answer = []
    clock = (CLOCKWISE, ANTICLOCKWISE)
    friends = tuple(permutations(dist))
    friends = friends[:len(friends)//2+1]
    for i in range(len(weak)):
        for di in clock:
            for friend in friends:
                print(friend)
                cnt = count_friend(i,di,weak,friend,n)
                if not cnt == -1:
                    answer.append(cnt)
    if len(answer) == 0:
        return -1
    return min(answer)

def get_distance(a,b,clockwise,n):
    if clockwise == CLOCKWISE:
        if a<b:
            return b-a
        else:
            return n-a+b
    else:
        if a>b:
            return a-b
        else:
            return n-b+a
def count_friend(start_weak_idx, clockwise, weak, dist, n):
    visit = set()
    p = start_weak_idx
    cnt = 0
    if len(weak) == 1:
        return 1
    for friend in dist:
        d = friend
        cnt += 1
        while d>-1:
            visit.add(weak[p])
            # 전체 외벽 점검 완료
            if len(visit) == len(weak):
                return cnt
            next_p = (p + clockwise) % len(weak)
            d -= get_distance(weak[p], weak[next_p], clockwise, n)
            p = next_p
            #다음 사람
            if d < 0:
                break
    if len(visit) < len(weak):
        return -1

print(solution(12,[1,5,6,10],[1,2,3,4]))
print(solution(12,[1,3,4,9,10],[3,5,7]))
print(solution(200,[0,100],[1,1]))