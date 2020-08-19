import sys
n = int(sys.stdin.readline())
l = [ 0 for _ in range(10001)]
for _ in range(n):
    val = int(sys.stdin.readline())
    l[val]+=1
for i in range(1,10001):
    if l[i]!=0:
        for _ in range(l[i]):
            print(i)



