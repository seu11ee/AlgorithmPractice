import numpy as np
T = int(input())
N,M = map(int,input().split())
for t in range(T):
    strBox=list()
    for n in range(N):
        strBox.append(list(input()))
        for i in range(N-M):
            if (strBox[n][i:i+M]==strBox[n][i+M-1:i-1:-1]):
                print("#%d"%(t+1),strBox[n][i:i+M])
    strBox = np.transpose(strBox)
    for n in range(N):
        for i in range(N - M):
        	if (strBox[n][i:i + M] ==strBox[n][i+M-1:i-1: -1]):
        		print("#%d" %(t+1), strBox[n][i:i + M])

#효원언니 풀이
T=int(input())
for i in range(T):
    result=[]
    N,M=map(int, input().split())
    for j in range(N):
        result.append(input())
    #가로
    for j in range(N):
        for k in range(N-M+1): #k가 M개 스트링의 시작 인덱스
            temp=''
            for l in range(M):
                temp+=result[j][k+l] #한 캐릭터씩
            if temp == temp[::-1]:
                r=temp
    #세로
    for j in range(N):
        for k in range(N-M+1):
            temp=''
            for l in range(M):
                temp+=result[k+l][j]
            if temp == temp[::-1]:
                r=temp
    print("#%d %s" % (i+1,r))