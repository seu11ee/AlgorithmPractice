from sys import stdin

inputStr = stdin.readline()

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

x = ord(inputStr[0])-96
y = int(inputStr[1])
answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx > 0 and nx < 9 and ny > 0 and ny < 9:
        answer += 1
print(answer)