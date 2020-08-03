from sys import stdin
from collections import Counter
def solution(clothes):
    answer = 1
    clothes2 = list()
    for i in clothes:
        clothes2.append(i[1])

    cnt = Counter(clothes2)
    if len(cnt) == 1:
        for j in cnt:
            print(cnt[j])
    else:


        for j in cnt.values():
            answer = answer * (j+1)

        print(answer-1)




solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])