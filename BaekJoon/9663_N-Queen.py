
n = int(input())

chess = [[0 for _ in range(n)] for _ in range(n)]
location = []
i = 0
cnt = 0
def queen(n,i):
    global cnt
    if i==n-1:
        cnt += 1
        location.pop()
        return cnt
    if i == 0:
        for k in range(n):
            location.append(k)
            queen(n,i+1)
    else:
        for k in range(n):
            temp = (i+1,k)
            #세로 겹침
            if k in location:
                continue
            else:
                for idx,val in enumerate(location):
                    if abs(idx-i)==abs(val-k):
                        continue
                    else:
                        location.append(k)
                        queen(n,i+1)
print(queen(n,i))