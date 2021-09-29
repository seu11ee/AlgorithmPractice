def solution(n, s):
    if s // n == 0:
        return [-1]
    multi_set = [s // n for _ in range(n)]

    sub_sum = (s // n) * n
    for i in range(n - (s - sub_sum), n):
        multi_set[i] += 1

    return multi_set