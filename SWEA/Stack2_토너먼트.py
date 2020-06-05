#아직이여
T = int(input())
def solution(n,l): #l 2차원은 학생번호,
    if n == 2:
        a = l[0][1]
        b = l[1][1]
        if (a == 1 and b == 3) or (a == 3 and b == 2) or (a == 2 and b == 1):
            return l[0]
        elif (a == 3 and b == 1) or (a == 2 and b == 3) or (a == 1 and b == 2):
            return l[1]
        else:
            return l[0]
    else:
        a = solution(n//2,l[:n//2])
        b = solution(n//2,l[n//2:])
        if (a[1] == 1 and b[1] == 3) or (a[1] == 3 and b[1] == 2) or (a[1] == 2 and b[1] == 1):
            return a[0]
        elif (a == 3 and b == 1) or (a == 2 and b == 3) or (a == 1 and b == 2):
            return b[0]
        else:
            return a[0]

for t in range(1,T+1):
    N = int(input())
    arr = list(enumerate(list(map(int,input().split())))) #enumerate 결과 튜플
    print("#%d %d"%(t,solution(N,arr)+1))