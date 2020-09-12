from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for order in orders:
        order = "".join(sorted(list(order)))
        answer.extend(list(map(lambda x: list(combinations(order,x)),range(2,len(order)+1))))
    answer = sum(answer,[])
    counter = list(Counter(answer).most_common())
    counter = sorted(counter,key = lambda x: (-x[1],len(x[0])))
    tempLen,tempCnt=2,2
    answer2 = []
    for i in counter:
        if len(i[0])>=tempLen and i[1] in course:
            if len(i[0])>tempLen:
                answer2.append("".join(sorted(i[0])))
                tempLen, tempCnt = len(i[0]), i[1]
            elif i[1]>=tempCnt:
                answer2.append("".join(sorted(i[0])))
                tempLen, tempCnt = len(i[0]), i[1]

    return sorted(answer2)
print(solution(["ABCFG","AC","CDE","ACDE","BCFG","ACDEH"],[2,3,4]))
print(solution(["ABCDE","AB","CD","ADE","XYZ","XYZ","ACD"],[2,3,5]))
print(solution(["XYZ","XWY","WXA"],[2,3,4]))