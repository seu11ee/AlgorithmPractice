'''
def solution(n):
    n -= 1
    l = ['1','2','4']
    answer = ''
    if n == 0 or n == 1 or n == 2:
        return l[n]
    else:
        while(n>=3):
            n ,temp = n//3 , n%3
            print("n",n)
            answer += l[temp]
        answer+=str(n)
        return answer[::-1]
'''
# 어려움
# level3
def solution(n):
    num = ['1', '2', '4']
    entire = num
    previous = num
    answer = ''

    while (n > len(entire)):
        print(len(entire))
        next = []
        length = len(previous)
        for i in range(3):
            for j in range(length):
                temp = num[i] + previous[j]
                entire.append(temp)
                next.append(temp)

        previous = next
    answer = entire[n - 1]
    return answer
print(solution(4))

