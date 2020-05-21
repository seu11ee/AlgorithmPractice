import sys
N = sys.stdin.readline()
for item in sorted(list(set(map(int,sys.stdin.readline().split())))):
    print(item,end=" ")