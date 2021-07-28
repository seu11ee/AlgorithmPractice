def solution(lines):
    answer = 0
    logs = []
    for line in lines:
        logs.append(list(findStartEnd(line)))
    for log in logs:
        answer = max(answer, calculateCnt(logs, log[0], log[0] + 1000), calculateCnt(logs, log[1], log[1] + 1000))
    return answer


def findStartEnd(line):
    hour = int(line[11:13])
    minute = int(line[14:16])
    second = float(line[17:23].replace(".",""))
    durations = float(line[24:].rstrip("s"))*1000
    end = (hour * 3600 + minute * 60) * 1000 + second
    start = end - durations + 1
    return start, end


def calculateCnt(logs, start, end):
    cnt = 0
    for log in logs:
        if log[1] >= start and log[0] < end:
            cnt += 1
    return cnt

# print(solution([
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))
# print(solution([
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
