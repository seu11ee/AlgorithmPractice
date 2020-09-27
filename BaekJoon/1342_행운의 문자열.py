import sys
from collections import Counter

def isLucky(s):
    temp=''
    answer = True
    for c in s:
        if temp == c:
            answer = False
            return answer
        else:
            temp = c
    return answer

s = sys.stdin.readline().rstrip()
counter = list(Counter(s).most_common())
#tuple의 list화
for i in range(len(counter)):
    counter[i] = [counter[i][0],counter[i][1]]
length = len(s)
ans = 0
def dfs(depth,prev):
    global ans, length
    if depth == length:
        ans += 1
        return
    for i in range(len(counter)):
        if counter[i][1] == 0:
            continue
        if counter[i][0] != prev:
            counter[i][1] -= 1
            dfs(depth+1,counter[i][0])
            counter[i][1] += 1

dfs(0,-1)
print(ans)

