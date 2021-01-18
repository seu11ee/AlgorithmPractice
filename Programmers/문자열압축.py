def solution(s):
    length = len(s)
    answer = []
    for i in range(length,0,-1):
        answer.append(check(s,i))

    return min(answer)

def check(s,l):
    cnt = 1
    cntList = []
    for i in range(0,len(s)-l+1,l):
        if s[i:i+l] == s[i+l:i+l+l]:
            cnt += 1
        else:
            if not cnt == 1:
                cntList.append(str(cnt))
            cnt = 1

    return sum(map(lambda x:len(x)+l,cntList)) + len(s)-sum(map(lambda x:l*int(x),cntList))