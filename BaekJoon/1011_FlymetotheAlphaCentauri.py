from sys import stdin

t = int(stdin.readline())
l = list()
for _ in range(t):
    l.append(tuple(map(int,stdin.readline().split())))
for test in l:
    x, y = test[0], test[1]
    n = y - x
    solution(n)
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 2
    elif n == 4:
        return 2