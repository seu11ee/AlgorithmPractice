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