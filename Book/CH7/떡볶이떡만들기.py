import sys
n,m = map(int,sys.stdin.readline().split())
dduks = list(map(int,sys.stdin.readline().split()))
dduks.sort()
start = dduks[0]
end = dduks[-1]
result = 0
while(start<=end):
    mid = (start+end)//2
    cnt = 0
    for dduk in dduks:
        cnt +=  dduk-mid if dduk-mid > 0 else  0
    #원하는 m만큼 찾음
    if cnt == m:
        result = mid
        break
    #m보다 작다 -> 높이를 더 줄여야 함
    elif cnt < m:
        end = mid - 1
    #m보다 크다 -> 정답의 후보가 됨
    else:
        result = mid
        start = mid + 1

print(result)


