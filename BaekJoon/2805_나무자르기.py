#binary search
import sys
#적절한 나무 높이를 셋팅하는 문제
n,m = map(int,sys.stdin.readline().split()) #m 만큼의 나무가 필요하다.
treeHeight = list(map(int,sys.stdin.readline().split()))
treeHeight.sort()
start = 0
end = treeHeight[-1]
 #target은 나무의 높이
answer = treeHeight[-1]
while start <= end:
    temp = 0
    mid = (start + end)//2
    for i in range(n):
        if treeHeight[i] >= mid:
            idx = i
            for j in treeHeight[idx:]:
                temp += j - mid
            break
    #temp에 저장하는 값은 얻을 수 있는 나무의 양
    if temp >= m :
        answer = mid
        start = mid + 1
    else:
        end = mid -1

print(answer)


