
def solution(n):
    answer = []
    num = n
    cnt = 1
    temp = 0
    breakPoint = 0
    while(True):
        if breakPoint >= n*(n+1)//2:
            break
        a = (cnt-1)*2
        for i in range(num):
            temp = temp+i+a
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
        cnt += 1
    print(answer)
    trueAnswer = [0 for _ in range(len(answer))]
    i = 1

    for index in answer:
        trueAnswer[index] = i
        i = i+1

    return trueAnswer
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))