from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    result = []
    for order in orders:
        for i in range(2, len(order) + 1):
            com = combinations(sorted(order), i)
            result.extend(com)
    cnt = Counter(result).most_common()
    most = dict()
    for c in cnt:
        length = len(c[0])
        count = c[1]
        if length in course and count > 1:
            if length not in most:
                most[length] = count
                answer.append("".join(c[0]))
            else:
                if most[length] == count:
                    answer.append("".join(c[0]))

    answer.sort()

    return answer