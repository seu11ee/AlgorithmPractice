def compareTime(a,b):
    aHour = a[0:2]
    aMin = a[3:5]
    bHour = b[0:2]
    bMin = b[3:5]
    if aHour > bHour:
        return True
    elif aHour < bHour:
        return False
    else:
        if aMin >= bMin:
            return True
        else:
            return False
def checkEmptySpace(space):
    for s in space:
        if not s == 0:
            return True
    return False
def makeTimeString(hour,min):
    timeString = ""
    if hour<10:
        timeString += "0%d"%hour
    else:
        timeString += "%d"%hour
    timeString += ":"
    if min < 10:
        timeString += "0%d"%min
    else:
        timeString += "%d"%min
    return timeString
def addTime(aHour,aMin,bHour,bMin):
    newHour = aHour + bHour
    newMin = aMin + bMin
    newHour += newMin//60
    newMin = newMin%60
    return makeTimeString(newHour,newMin)

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort(reverse=True)
    space = [ m for _ in range(n)]
    firstHour = 9
    firstMin = 0
    last = timetable[-1]
    #일단 크루들 다 태워봄
    for i in range(n):
        now = addTime(firstHour,firstMin,0,t*i)

        for crew in timetable[::-1]:
            #현재시간 전에 도착한 크루가 있다면
            if compareTime(now,crew):
                space[i] -= 1
                last = timetable.pop()
                if space[i] == 0:
                    break
            else:
                break
        if not timetable:
            break
    if checkEmptySpace(space[i:]):
        answer = addTime(firstHour,firstMin,0,t*(n-1))
    else:
        if last[3:5] == "00":
            answer = makeTimeString(int(last[0:2]) - 1, 59)
        else:
            answer = makeTimeString(int(last[0:2]), int(last[3:5]) - 1)
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))
print(solution(1, 1, 5, ["00:00", "00:00", "00:00", "00:00", "00:01", "00:02", "00:03", "00:04"])) # "00:00"))