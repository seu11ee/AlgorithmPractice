# #메모리 초과
#
# import sys
#
# N = int(sys.stdin.readline())
# l = list(permutations(range(1,N+1),N))
#
# num = tuple(map(int,sys.stdin.readline().rstrip().split()))
#
# index = l.index(num)
# if num == tuple(range(N,0,-1)):
#     print(-1)
# else:
#     for i in range(N):
#         print(l[index+1][i],end = " ")

#<permutation 라이브러리 안 쓰는 경우>
import sys
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
if (N==1):
    print(-1)
for i in range(N-1,0,-1):
    if l[i-1]<l[i]: #앞에 수가 작은 경우 걸림
        for j in range(N-1,i-1,-1): #뒤에서 부터 i-1보다 큰수를 찾는다
            if l[j]>l[i-1]:
                l[i-1],l[j] = l[j],l[i-1] #찾으면 swap해줌
                break
        l[i:] = sorted(l[i:]) #i-1뒤로 오름차순 정렬해준다
        for k in l:
            print(k,end = " ")
        break
    else:
        if i ==1 :
            print(-1)
#<permutations 라이브러리 쓰는 경우>
# import sys
# from itertools import permutations
#
# N = int(sys.stdin.readline())
# l = list(map(int,sys.stdin.readline().split()))
# #print(N)
# if (N==1):
#     print(-1)
# for i in range(N-1,0,-1):
#     if l[i-1]<l[i]:
#         p = list(permutations(l[i-1:]))
#         p.sort()
#         idx = p.index(tuple(l[i-1:]))
#         l[i-1:]=p[idx+1]
#         for j in l:
#             print(j, end=" ")
#         break
#     else:
#         if i==1:
#             print(-1)

'''
세화풀
n = int(input())
a = list(map(int, input().split()))

def next_permutation(a):
    n = len(a)-1
    i = n이 #i는 인덱스
    while i>0 and a[i-1]>=a[i]:
        i-=1
       
    if i==0:
        return False
        

    j = n
    while a[i-1]>=a[j]:
        j-=1
    a[i-1],a[j]=a[j],a[i-1]
    
    j=n
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    return True

if next_permutation(a) is True:
    for i in a:
        print(i, end=' ')
    print()
else:
    print(-1)
    '''