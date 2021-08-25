def solution(play_time, adv_time, logs):
    play_time = to_sec(play_time)
    adv_time = to_sec(adv_time)
    memo = [0 for _ in range(play_time+2)]
    for log in logs:
        log_start,log_end = log.split("-")
        log_start = to_sec(log_start)
        log_end = to_sec(log_end)
        memo[log_start+1] += 1
        memo[log_end+1] -= 1
    for i in range(1,len(memo)):
        memo[i] = memo[i-1]+memo[i]
    for i in range(1,len(memo)):
        memo[i] = memo[i-1]+memo[i]
    # print(memo)
    most_views = memo[adv_time-1]
    answer = 0
    for i in range(1,play_time-adv_time+1):
        temp = memo[i+adv_time]-memo[i]
        if temp > most_views:
            most_views = temp
            answer = i
    return to_time(answer)
def to_sec(time):
    h,m,s = map(int, time.split(":"))
    return h*3600+m*60+s
def to_time(sec):
    return "%02d:%02d:%02d"%(sec//3600,(sec%3600)//60,sec%3600%60)
print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
#"01:30:59"
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
#"01:00:00"
print(solution("00:0:30","00:00:02",["00:00:01-00:00:04","00:00:03-00:00:06"]))