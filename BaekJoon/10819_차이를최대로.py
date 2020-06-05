import sys
from collections import deque
n = int(sys.stdin.readline())
A = deque(map(int, sys.stdin.readline().split()))
sorted(A)
sum=0
while(A):
    a = A.pop()
    if (A):
        b = A.popleft()
    else:
        sum +=
    if (A):
        c = A.pop()
    A.append(c)
    sum = sum + abs(a-b) +abs(b-c)
print(sum)