import sys
n,k = map(int,sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
coin.sort(reverse = True)
change = k
answer = 0
for c in coin:
    temp = change//c
    if temp > 0:
        answer += temp
        change = change - temp * c
print(answer)
