import sys
K, N = map(int,sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
lan.sort()
start = 1
end = lan[-1]
while start <= end:

    mid = (start + end)//2

    for i in range(len(lan)):
        if lan[i]>=mid:
            idx = i
            break
    sum = 0
    for line in lan[idx:]:
        sum += (line//mid)
    if sum >= N :
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)


