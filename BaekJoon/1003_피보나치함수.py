'''
<시간초과>
import sys
T = int(sys.stdin.readline())

def fibonacci(n):
    global count0,count1
    if n==0:
        count0+=1
        return 0
    elif n==1:
        count1+=1
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for _ in range(T):
    N = int(sys.stdin.readline())
    count0=0
    count1=0
    fibonacci(N)
    print(count0,count1)
'''
import sys
T = int(sys.stdin.readline())
arr=[[1,0],[0,1]]
for i in range(2,41):
    arr.append([arr[i-2][0]+arr[i-1][0],arr[i-2][1]+arr[i-1][1]])
for _ in range(T):
    N = int(sys.stdin.readline())
    print(arr[N][0],arr[N][1])

