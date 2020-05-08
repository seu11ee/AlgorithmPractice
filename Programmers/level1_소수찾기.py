import math
def solution(n):
    MAX = 1000000
    prime=[True]*(MAX+1)
    prime[1] = False
    ceiling = math.ceil(math.sqrt(MAX))
    for i in range(2,ceiling):
        if prime[i]:
            for j in range(i*2,MAX+1,i):
                prime[j] = False
    count = 0
    for num in range(1,n+1):
        if prime[num]:
            count+=1
    return count
print(solution(10),solution(5))
