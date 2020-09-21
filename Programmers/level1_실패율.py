from collections import Counter
def solution(N, stages):
    answer = []
    fail = [[i,0,1]for i in range(1,N+1)]
    cnt = sorted(list(Counter(stages).most_common()),reverse = True)
    #print(cnt)
    length = len(cnt)
    if cnt[0][0] != N+1:
        fail[cnt[0][0]-1] = [cnt[0][0],1,1]
    temp = cnt[0][1]
    for i in range(1,length):
        stage = cnt[i][0]
        stage_cnt = cnt[i][1]from collections import Counter
def solution(N, stages):
    answer = []
    fail = [[i,0,1]for i in range(1,N+1)]
    cnt = sorted(list(Counter(stages).most_common()),reverse = True)
    #print(cnt)
    length = len(cnt)
    if cnt[0][0] != N+1:
        fail[cnt[0][0]-1] = [cnt[0][0],1,1]
    temp = cnt[0][1]
    for i in range(1,length):
        stage = cnt[i][0]
        stage_cnt = cnt[i][1]
        fail[stage-1] = [stage,stage_cnt,temp+stage_cnt]
        temp = temp + stage_cnt
    fail.sort(key = lambda x:(-(x[1]/x[2]),x[0]))

    for i in fail:
        answer.append(i[0])
    return answer
        fail[stage-1] = [stage,stage_cnt,temp+stage_cnt]
        temp = temp + stage_cnt
    fail.sort(key = lambda x:(-(x[1]/x[2]),x[0]))

    for i in fail:
        answer.append(i[0])
    return answer
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))