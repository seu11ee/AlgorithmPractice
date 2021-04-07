from sys import stdin
n = int(stdin.readline())
answer = 0
has3 = 60*60
notHas3 = 15*60*2-15*15
for i in range(n+1):
    if i % 10 == 3 or i / 10 == 3:
        answer += has3
    else:
        answer += notHas3
print(answer)
