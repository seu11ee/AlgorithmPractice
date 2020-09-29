import sys

n = int(sys.stdin.readline())

l = [int(sys.stdin.readline()) for _ in range(n)]
for i in sorted(list(set(l)),reverse=True):
    print(i)

