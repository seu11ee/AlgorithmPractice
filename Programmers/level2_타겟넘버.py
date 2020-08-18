from itertools import product
def solution(numbers,target):
    cnt = 0
    for t in product([1,-1],repeat = len(numbers)):
        sum = 0
        idx = 0
        for i in t:
            sum += numbers[idx]*i
            idx += 1
        if sum == target:
            cnt += 1
    return cnt
print(solution([1,1,1,1,1],3))