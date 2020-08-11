import sys
n = int(sys.stdin.readline())
myList = []
for _ in range(n):
    myList.append(tuple(map(int,sys.stdin.readline().split())))
myList.sort()
for val1,val2 in myList:
    print("%d %d"%(val1,val2))