
def solution(n):
    answer = []
    num = n
    cnt = 1
    temp = 0
    breakPoint = 0
    while(True):
        if breakPoint >= n*(n+1)//2:
            break
        for i in range(num):
            temp = temp+i*cnt
            answer.append(temp)
            breakPoint += 1
        for i in range(num-1):
            temp = temp + 1
            answer.append(temp)
            breakPoint += 1

        for i in range(n-cnt+1,n-cnt+3-num,-1):
            temp = temp - i
            answer.append(temp)
            breakPoint += 1
        num = num - 3
        temp = temp +2*cnt
        cnt += 1

    trueAnswer = [0 for _ in range(n*(n+1)//2)]
    i = 1

    for index in answer:
        trueAnswer[index] = i
        i = i+1

    return trueAnswer