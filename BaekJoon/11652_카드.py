import sys
from collections import Counter
n = int(sys.stdin.readline())
cardList = list()
for _ in range(n):
    cardList.append(int(sys.stdin.readline()))
t = tuple(Counter(cardList).most_common())
minNum = t[0][0]
if len(t)>1 and t[0][1] == t[1][1]:
    maxCnt = t[0][1]

    i = 1

    while(True):
        if i == len(t):
            break
        if maxCnt != t[i][1]:
            break
        if minNum>t[i][0]:
            minNum = t[i][0]
        i += 1
print(minNum)


