from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque()
for _ in range(n):
    queue.append(list(map(int,stdin.readline().split())))
while(len(queue)>1):
    bottom = queue.pop()
    top = queue.pop()
    for i in range(len(top)):
        top[i]+=max(bottom[i],bottom[i+1])
    queue.append(top)
print(top[0])
