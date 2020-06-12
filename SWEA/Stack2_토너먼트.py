
import math
T = int(input())
def solution(l): #l 2차원은 학생번호,
    n = len(l)
    #print(l)
    if n == 2:
        a = l[0] #리스트의 첫번째 학생 순서쌍
        b = l[1] #리스트의 두번째 학생 순서쌍
        if (a[1] == 1 and b[1] == 3) or (a[1] == 3 and b[1] == 2) or (a[1] == 2 and b[1] == 1):
            return l[0] #리스트의 첫번째 학생 튜플 리
        elif (a[1] == 3 and b[1]== 1) or (a[1] == 2 and b[1] == 3) or (a[1] == 1 and b[1] == 2):
            return l[1]
        else:
            return l[0]
    elif n == 1:
        return l[0]
    #1<2 1>3 2>1 2<3 3<1 3>2 가위바위보ㅗㅗㅗㅗ
    else:
        a = solution(l[:math.ceil(n/2)])
        b = solution(l[math.ceil(n/2):])
        if (a[1] == 1 and b[1] == 3) or (a[1] == 3 and b[1] == 2) or (a[1] == 2 and b[1] == 1):
            return a
        elif (a[1] == 3 and b[1] == 1) or (a[1] == 2 and b[1] == 3) or (a[1] == 1 and b[1] == 2):
            return b
        else:
            return a

for t in range(1,T+1):
    N = int(input())
    input_list=list(map(int,input().split()))
    arr = list(enumerate(input_list)) #enumerate 결과 튜플
    print("#%d"%t,solution(arr)[0]+1)