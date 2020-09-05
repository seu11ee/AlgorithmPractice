import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a = list(set(a))
a.sort()
for val in a:
    print(val)

