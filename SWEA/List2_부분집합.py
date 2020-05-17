'''N개의 원소의 부분집합의 합이 K가 되는 경우 찾기'''

T = int(input())
A = list(range(1,13))
l = len(A)
for i in range(1,T+1):
    N,K = map(int,input().split())
    count = 0
    for j in range(1<<l):
        temp = []
        for k in range(l):
            if j&(1<<k):
                temp.append(A[k])
        if (sum(temp) == K )and (len(temp)==N):
            count += 1
    print("#%d %d"%(i,count))