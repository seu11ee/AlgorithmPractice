from itertools import combinations
from collections import Counter

def toAlpha(b):
    b = bin(b)
    b= b[2:]
    b= b[::-1]
    l = list(b)
    ans = ""
    for idx, val in enumerate(l):
        if val == '1':
            ans += chr(65 + idx)
    return ans

def solution(orders, course):
    answer = []
    #주문 비트화
    bitOrders = []
    for customers in orders:
        newBit = 0
        for i in customers:
            newBit = newBit | 2**int(ord(i)-ord('A'))
        bitOrders.append(newBit)
    l = len(bitOrders)
    temp = []
    for i in range(l-1):
        for j in range(i+1,l):
            t = bitOrders[i] & bitOrders[j]
            print(toAlpha(t))
            temp.append(t)
    counter = list(Counter(temp).most_common())
    counter.reverse()


    print(list(map(lambda x:toAlpha(x[0]),counter)))
    for i in counter:
        t = bin(i[0]).count('1')
        if t in course:
            answer.append(i)
    answer2 = []
    for ans in answer:

        a = toAlpha(ans[0])
        #알파벳화
        answer2.append(("".join(sorted(list(a))),ans[1]))
        answer2.sort()

    return answer2
#print(solution(["ABCFG","AC","CDE","ACDE","BCFG","ACDEH"],[2,3,4]))
print(solution(["ABCDE","AB","CD","ADE","XYZ","XYZ","ACD"],[2,3,5]))
#print(solution(["XYZ","XWY","WXA"],[2,3,4]))