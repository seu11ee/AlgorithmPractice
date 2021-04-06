from sys import stdin

n, k = map(int, stdin.readline().split())
cnt = 0
while(True):
    if n == 1:
        break
    cnt += 1
    if n % k == 0:
        n /= k
    else:
        n -= 1
print(cnt)